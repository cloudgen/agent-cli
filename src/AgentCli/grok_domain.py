# =============================================================================
# xAI grok install, session, and auth deposit.
# requirement-domain-agent-cli — verbs, deposit, sudoer JSON, setup channel.
# requirement-grok-auth-backup — session words and sync skip.
# requirement-shell-cli-storage — scratch files go through class Storage.
# requirement-python-oop — class GrokDomain. No module-level helpers.
# Peer binary stays grok. Auth files stay under ~/.grok.
# This module does not run a vendor shell installer.
# =============================================================================
from __future__ import annotations

import datetime
import glob
import json
import os
import platform
import shutil
import subprocess

from .host import Host
from .output import Output
from .shell_startup import ShellStartup
from .storage import Storage


class GrokDomain:
    """Install and run the peer grok binary, and back up its auth files."""

    APP_NAME = "agent-cli"
    DEPOSIT = "/var/agent-cli"
    GLOBAL_BIN = "/usr/local/bin"
    VENDOR_BASE = "https://x.ai/cli"
    VENDOR_FALLBACK = "https://storage.googleapis.com/grok-build-public-artifacts/cli"
    CHANNEL = "stable"
    PROMPT_TIMEOUT = 14
    SESSION_WORDS = ("valid", "timeout", "invalid", "missing")

    def __init__(
        self,
        output=None,
        storage=None,
        host=None,
        session_override=None,
        deposit_root=None,
        environ=None,
        runner=None,
        grok_home=None,
        logger=None,
        version="",
    ):
        self.environ = os.environ if environ is None else environ
        self.logger = logger
        if logger is not None:
            logger.log_message("instantiated", component="GrokDomain")
        self.output = output if output is not None else Output()
        self.storage = storage if storage is not None else Storage(
            app_name=self.APP_NAME, environ=self.environ
        )
        self.host = host if host is not None else Host(environ=self.environ)
        self.session_override = session_override
        self.deposit_root = deposit_root or self.environ.get("AGENT_CLI_DEPOSIT") or self.DEPOSIT
        self.runner = runner
        self.grok_home = grok_home
        self.startup = ShellStartup(
            version=version,
            output=self.output,
            environ=self.environ,
            logger=logger,
            host=self.host,
        )

    def global_bin(self) -> str:
        root = self.environ.get("AGENT_CLI_GLOBAL_BIN", self.GLOBAL_BIN)
        return os.path.join(root, self.APP_NAME)

    def invoking_home(self) -> str:
        sudo_user = self.environ.get("SUDO_USER", "")
        if hasattr(os, "geteuid") and os.geteuid() == 0 and sudo_user:
            try:
                import pwd
                return pwd.getpwnam(sudo_user).pw_dir
            except (ImportError, KeyError):
                pass
        return self.environ.get("HOME") or "/tmp"

    def auth_home(self) -> str:
        if self.grok_home:
            return self.grok_home
        if os.geteuid() == 0 and self.environ.get("SUDO_USER"):
            return os.path.join(self.invoking_home(), ".grok")
        return os.path.join(self.environ.get("HOME") or "/tmp", ".grok")

    def peer_path(self) -> str:
        override = self.environ.get("AGENT_CLI_GROK_BIN", "")
        if override:
            return override
        found = shutil.which("grok")
        if found:
            return found
        return os.path.join(self.auth_home(), "bin", "grok")

    def session_word(self) -> str:
        """valid, timeout, invalid, or missing. Timeout is not logged-out."""
        if self.session_override in self.SESSION_WORDS:
            return self.session_override
        forced = self.environ.get("AGENT_CLI_SESSION", "")
        if forced in self.SESSION_WORDS:
            return forced
        if self.host.is_termux():
            return self._session_from_local_auth()
        return self._session_from_probe()

    def logged_in(self) -> bool:
        """A timeout is still treated as signed-in. Invalid and missing are not."""
        return self.session_word() in ("valid", "timeout")

    def _session_from_local_auth(self) -> str:
        path = os.path.join(self.auth_home(), "auth.json")
        if not os.path.isfile(path) or os.path.getsize(path) == 0:
            return "missing"
        try:
            with open(path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, ValueError):
            return "invalid"
        if not isinstance(data, dict) or not data:
            return "invalid"
        if data.get("refresh_token") or data.get("key") or data.get("expires_at"):
            return "valid"
        return "invalid"

    def _session_from_probe(self) -> str:
        peer = self.peer_path()
        if not peer or not os.path.isfile(peer) or not os.access(peer, os.X_OK):
            return "missing"
        if self.runner is not None:
            code = self.runner(["probe", peer])
            if code == 0:
                return "valid"
            if code in (124, 137):
                return "timeout"
            return "invalid"
        try:
            proc = subprocess.run(
                [peer, "-p", "hello"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=self.PROMPT_TIMEOUT,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return "timeout"
        except OSError:
            return "missing"
        if proc.returncode == 0:
            return "valid"
        if proc.returncode in (124, 137):
            return "timeout"
        return "invalid"

    def check_session(self) -> int:
        word = self.session_word()
        return self.output.ok("check-session", word, {"session": word})

    def backup(self) -> int:
        """Re-enter as root when this process is not root. Tests call _deposit."""
        if os.geteuid() != 0 and self.environ.get("AGENT_CLI_BACKUP_AS_ROOT") != "1":
            binary = self.global_bin()
            if self.environ.get("AGENT_CLI_BACKUP_NO_SUDO") == "1":
                return self._deposit()
            return self.output.error(
                "backup deposits auth files as root.",
                "sudo -n {0} backup".format(binary),
            )
        return self._deposit()

    def _deposit(self) -> int:
        source = self.auth_home()
        names = sorted(glob.glob(os.path.join(source, "auth.*")))
        if not names:
            return self.output.error(
                "No auth files under {0}.".format(source),
                "agent-cli setup",
            )
        try:
            os.makedirs(self.deposit_root, mode=0o755, exist_ok=True)
        except OSError as exc:
            return self.output.error(
                "Cannot create deposit {0}.".format(self.deposit_root),
                "sudo -n {0} backup".format(self.global_bin()),
            )
        copied = []
        for path in names:
            base = os.path.basename(path)
            dest = os.path.join(self.deposit_root, base)
            try:
                shutil.copy2(path, dest)
                os.chmod(dest, 0o644)
            except OSError:
                return self.output.error(
                    "Cannot write {0}.".format(dest),
                    "sudo -n {0} backup".format(self.global_bin()),
                )
            copied.append(base)
        return self.output.ok(
            "backup",
            "Deposited {0}.".format(", ".join(copied)),
            {"deposit": self.deposit_root, "files": copied},
        )

    def sync_auth(self) -> int:
        if self.logged_in():
            return self.output.ok(
                "sync-auth",
                "No sync-auth for logged-in environment.",
                {"reason": "logged-in"},
            )
        return self._copy_deposit_to_home()

    def _copy_deposit_to_home(self) -> int:
        names = sorted(glob.glob(os.path.join(self.deposit_root, "auth.*")))
        if not names:
            return self.output.error(
                "Deposit {0} has no auth files.".format(self.deposit_root),
                "agent-cli backup",
            )
        dest_root = self.auth_home()
        try:
            os.makedirs(dest_root, mode=0o700, exist_ok=True)
        except OSError:
            return self.output.error(
                "Cannot create {0}.".format(dest_root),
                "agent-cli sync-auth",
            )
        for path in names:
            dest = os.path.join(dest_root, os.path.basename(path))
            shutil.copy2(path, dest)
            if os.path.basename(path) == "auth.json":
                os.chmod(dest, 0o600)
        return self.output.ok("sync-auth", "Restored auth files into {0}.".format(dest_root))

    def sync_from_remote(self, spec: str) -> int:
        if self.logged_in():
            return self.output.ok(
                "sync-auth-from-remote",
                "No sync-auth for logged-in environment.",
                {"reason": "logged-in"},
            )
        if not spec or "@" not in spec:
            return self.output.error(
                "sync-auth-from-remote needs user@host.",
                "agent-cli sync-auth-from-remote user@host",
            )
        return self.output.error(
            "Remote fetch is not run from this process without AGENT_CLI_SCP.",
            "agent-cli sync-auth-from-remote {0}".format(spec),
        )

    def sync_to_remote(self, spec: str) -> int:
        if not spec or "@" not in spec:
            return self.output.error(
                "sync-auth-to-remote needs user@host.",
                "agent-cli sync-auth-to-remote user@host",
            )
        return self.output.ok(
            "sync-auth-to-remote",
            "Type: agent-cli sync-auth-to-remote {0}".format(spec),
            {"spec": spec},
        )

    def detect_platform(self) -> str:
        forced = self.environ.get("AGENT_CLI_PLATFORM", "")
        if forced:
            return forced
        system = platform.system()
        if system == "Darwin":
            os_name = "macos"
        elif system == "Linux":
            os_name = "linux"
        elif system.startswith("MINGW") or system.startswith("MSYS") or system.startswith("CYGWIN"):
            os_name = "windows"
        else:
            return ""
        machine = platform.machine().lower()
        if machine in ("x86_64", "amd64"):
            arch = "x86_64"
        elif machine in ("arm64", "aarch64"):
            arch = "aarch64"
        else:
            return ""
        return "{0}-{1}".format(os_name, arch)

    def setup(self, force=False, interactive=False) -> int:
        """Point at the vendor channel, then the public fallback. Do not run a shell installer."""
        token = self.detect_platform()
        if not token:
            return self.output.error(
                "This host is not linux, macos, or windows on x86_64 or aarch64.",
                "agent-cli about",
            )
        peer = self.peer_path()
        installed = os.path.isfile(peer) and os.access(peer, os.X_OK)
        if installed and not force:
            if interactive:
                return self.output.ok(
                    "setup",
                    "grok is already installed. Choose keep, reinstall, or exit.",
                    {"choices": ["keep", "reinstall", "exit"], "peer": peer},
                )
            return self.output.ok(
                "setup",
                "grok is already installed at {0}.".format(peer),
                {"peer": peer, "skipped": True},
            )
        if shutil.which("curl") is None and self.runner is None:
            return self.output.error(
                "curl is required to download grok.",
                "Install curl, then agent-cli setup",
            )
        version = self._read_pointer(self.VENDOR_BASE) or self._read_pointer(self.VENDOR_FALLBACK)
        if not version:
            return self.output.error(
                "The grok version pointer could not be read.",
                "agent-cli setup --force",
            )
        dest_dir = os.path.join(self.auth_home(), "downloads")
        try:
            os.makedirs(dest_dir, mode=0o700, exist_ok=True)
        except OSError:
            return self.output.error(
                "Cannot create {0}.".format(dest_dir),
                "agent-cli setup",
            )
        artifact = "grok-{0}-{1}".format(version, token)
        saved = self._fetch_artifact(version, artifact, dest_dir)
        if not saved:
            return self.output.error(
                "The grok artifact could not be downloaded.",
                "agent-cli setup --force",
            )
        if not self._smoke(saved):
            return self.output.error(
                "The downloaded grok binary did not run.",
                "agent-cli setup --force",
            )
        bin_dir = os.path.join(self.auth_home(), "bin")
        os.makedirs(bin_dir, mode=0o700, exist_ok=True)
        link = os.path.join(bin_dir, "grok")
        if os.path.lexists(link):
            os.remove(link)
        shutil.copy2(saved, link)
        os.chmod(link, 0o755)
        if self.host.is_termux():
            self.write_exec_wrapper(link)
        return self.output.ok("setup", "Installed grok {0}.".format(version), {"peer": link})

    def _read_pointer(self, base: str) -> str:
        url = "{0}/{1}".format(base.rstrip("/"), self.CHANNEL)
        if self.runner is not None:
            text = self.runner(["pointer", url])
            if not isinstance(text, str) or not text.strip():
                return ""
            return text.splitlines()[0].strip()
        try:
            proc = subprocess.run(
                ["curl", "-fsSL", url],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                timeout=30,
                check=False,
                universal_newlines=True,
            )
        except (OSError, subprocess.TimeoutExpired):
            return ""
        if proc.returncode != 0 or not proc.stdout:
            return ""
        return proc.stdout.splitlines()[0].strip()

    def _fetch_artifact(self, version: str, artifact: str, dest_dir: str) -> str:
        for suffix in (".zst", ".gz", ""):
            name = artifact + suffix
            for base in (self.VENDOR_BASE, self.VENDOR_FALLBACK):
                url = "{0}/{1}/{2}".format(base.rstrip("/"), version, name)
                dest = os.path.join(dest_dir, name)
                if self.runner is not None:
                    body = self.runner(["fetch", url, dest])
                    if body:
                        return dest
                    continue
                try:
                    proc = subprocess.run(
                        ["curl", "-fsSL", "-o", dest, url],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        timeout=120,
                        check=False,
                    )
                except (OSError, subprocess.TimeoutExpired):
                    continue
                if proc.returncode == 0 and os.path.isfile(dest) and os.path.getsize(dest) > 0:
                    return dest
        return ""

    def _smoke(self, path: str) -> bool:
        if self.runner is not None:
            return bool(self.runner(["smoke", path]))
        try:
            proc = subprocess.run(
                [path, "--version"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=30,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            return False
        return proc.returncode == 0

    def write_exec_wrapper(self, binary: str) -> str:
        """Android subset: opt out of start-services and kill proot on exit."""
        wrapper = binary + ".wrap"
        body = (
            "#!/bin/sh\n"
            "unset LD_PRELOAD\n"
            "export TERMUX_EXEC_OPTOUT=1\n"
            "if command -v proot >/dev/null 2>&1; then\n"
            "  exec proot --kill-on-exit "
            '-b /dev/null:"$PREFIX/var/service/start-services.sh" '
            '-b /etc/resolv.conf:/etc/resolv.conf "%s" "$@"\n'
            "fi\n"
            'exec "%s" "$@"\n'
        ) % (binary, binary)
        with open(wrapper, "w", encoding="utf-8") as handle:
            handle.write(body)
        os.chmod(wrapper, 0o755)
        return wrapper

    def update_grok(self) -> int:
        return self.setup(force=True, interactive=False)

    def reinstall(self) -> int:
        peer = self.peer_path()
        link = os.path.join(self.auth_home(), "bin", "grok")
        for path in (peer, link):
            if path and os.path.lexists(path) and not os.path.basename(path).startswith("auth."):
                try:
                    os.remove(path)
                except OSError:
                    return self.output.error(
                        "Cannot remove {0}.".format(path),
                        "agent-cli reinstall",
                    )
        return self.setup(force=True, interactive=False)

    def run(self, args=None) -> int:
        peer = self.peer_path()
        if not os.path.isfile(peer):
            return self.output.error(
                "grok is not installed.",
                "agent-cli setup",
            )
        argv = [peer] + list(args or [])
        if self.runner is not None:
            code = self.runner(argv)
            return int(code) if isinstance(code, int) else 0
        try:
            proc = subprocess.run(argv, check=False)
        except OSError:
            return self.output.error("Could not start grok.", "agent-cli setup")
        return int(proc.returncode)

    def crontab_lines(self) -> tuple:
        binary = self.global_bin()
        backup = self.environ.get(
            "AGENT_CLI_CRON_BACKUP",
            "*/30 * * * * sudo {0} backup".format(binary),
        )
        sync = self.environ.get(
            "AGENT_CLI_CRON_SYNC",
            "45 * * * * {0} sync-auth".format(binary),
        )
        return backup, sync

    def add_crontab(self) -> int:
        binary = self.global_bin()
        if not os.path.isfile(binary) or not os.access(binary, os.X_OK):
            if self.environ.get("AGENT_CLI_ASSUME_BIN") != "1":
                return self.output.error(
                    "The global binary is not executable.",
                    "Install {0}, then agent-cli add-crontab".format(binary),
                )
        if self.environ.get("AGENT_CLI_SUDO_GRANT") != "1":
            return self.output.error(
                "The backup sudoers grant is missing.",
                "agent-cli generate-sudoer-request",
            )
        backup, sync = self.crontab_lines()
        return self.output.ok(
            "add-crontab",
            "{0}\n{1}".format(backup, sync),
            {"backup": backup, "sync": sync},
        )

    def sudoer_document(self, action="add", username=None) -> dict:
        user = username or self.environ.get("USER") or self.environ.get("USERNAME") or "unknown"
        if action not in ("add", "update"):
            action = "add"
        purpose = "Allow {0} to run {1} backup as root.".format(user, self.APP_NAME)
        return {
            "schema_version": 1,
            "purpose": purpose,
            "username": user,
            "service": self.APP_NAME,
            "action": action,
            "commands": [
                {
                    "runas": "root",
                    "tags": ["NOPASSWD"],
                    "path": self.global_bin(),
                    "args": ["backup"],
                }
            ],
        }

    def sudoer_text(self, username=None) -> str:
        doc = self.sudoer_document(username=username)
        return "\n".join([
            "# Purpose: {0}".format(doc["purpose"]),
            "{0} ALL=(root) NOPASSWD: {1} backup".format(doc["username"], doc["commands"][0]["path"]),
            "",
        ])

    def print_sudoers(self) -> int:
        text = self.sudoer_text()
        if self.output.json_mode:
            return self.output.ok("print-sudoers", text.strip())
        print(text, end="")
        return 0

    def print_sudoers_install_script(self) -> int:
        user = self.environ.get("USER") or "unknown"
        path = "/etc/sudoers.d/{0}-{1}".format(self.APP_NAME, user)
        script = "sudo install -m 0440 ./sudoers.fragment {0}\nsudo visudo -c -f {0}\n".format(path)
        if self.output.json_mode:
            return self.output.ok("print-sudoers-install-script", script.strip())
        print(script, end="")
        return 0

    def generate_sudoer_request(self, directory=None, action="add") -> int:
        doc = self.sudoer_document(action=action)
        folder = directory or os.getcwd()
        stamp = datetime.date.today().strftime("%Y%m%d")
        number = 1
        while True:
            base = "sudoer-{0}-{1}-{2}-{3}-{4}.json".format(
                stamp, self.APP_NAME, doc["username"], doc["action"], number
            )
            path = os.path.join(folder, base)
            if not os.path.exists(path):
                break
            number += 1
        try:
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(doc, handle, indent=2)
                handle.write("\n")
        except OSError:
            return self.output.error(
                "Cannot write the sudoer request.",
                "agent-cli generate-sudoer-request",
            )
        return self.output.ok("generate-sudoer-request", path, {"path": path})

    def submit_sudoer_request(self, path="") -> int:
        if not path:
            return self.output.error(
                "submit-sudoer-request needs the JSON file.",
                "agent-cli generate-sudoer-request",
            )
        return self.output.error(
            "No sudoer submission tool is configured.",
            "agent-cli print-sudoers-install-script",
        )

    def remove_project_sudoers(self) -> int:
        user = self.environ.get("USER") or "unknown"
        path = "/etc/sudoers.d/{0}-{1}".format(self.APP_NAME, user)
        return self.output.ok(
            "remove-project-sudoers",
            "Type: sudo rm {0}".format(path),
            {"path": path},
        )

    def install_startup(self) -> int:
        """User-bin companion. Writes this login's startup files. Does not call pip."""
        self.startup.path_add_shell()
        return 0

    def uninstall_startup(self, force=False) -> int:
        """Strip this product's stickers when --force is set. Does not delete the files."""
        if not force:
            return self.output.error(
                "uninstall edits this login's startup-file stickers.",
                "agent-cli uninstall --force",
            )
        self.startup.cleanup_path()
        return self.output.ok(
            "uninstall",
            "Removed this product's startup-file stickers. Type: agent-cli self-uninstall --force",
        )

    def rc_test(self, root, file_name="bashrc", case="create", feature="") -> int:
        """Fixture writer. Does not call install or setup."""
        return self.startup.path_rc_test(root, file_name or "bashrc", case or "create", feature)

    def where_is_me(self) -> int:
        binary = self.global_bin()
        peer = self.peer_path()
        message = "agent-cli: {0}\ngrok: {1}".format(binary, peer)
        return self.output.ok("where-is-me", message, {"agent_cli": binary, "grok": peer})

    def menu_text(self, kind: str) -> str:
        """Result page for a menu row. Remote and setup choices stay on the terminal."""
        if kind in ("sync-auth-from-remote", "sync-auth-to-remote"):
            return "Type: agent-cli {0} user@host".format(kind)
        if kind == "setup":
            peer = self.peer_path()
            if os.path.isfile(peer):
                return "grok is already installed. Choose keep, reinstall, or exit.\nType: agent-cli setup"
            return "Type: agent-cli setup"
        if kind == "run":
            return "Type: agent-cli run"
        if kind == "backup":
            return "Type: sudo -n agent-cli backup"
        if kind == "add-crontab":
            backup, sync = self.crontab_lines()
            return "{0}\n{1}".format(backup, sync)
        if kind in ("version-check", "self-update", "self-uninstall", "self-install"):
            return kind
        if kind == "where-is-me":
            return "agent-cli: {0}\ngrok: {1}".format(self.global_bin(), self.peer_path())
        if kind == "check-session":
            return self.session_word()
        if kind == "reinstall":
            return "Type: agent-cli reinstall"
        if kind == "update-grok":
            return "Type: agent-cli update-grok"
        return "Type: agent-cli {0}".format(kind)

    def dispatch(self, verb: str, args=None, force=False) -> int:
        args = list(args or [])
        if verb == "check-session":
            return self.check_session()
        if verb == "backup":
            return self.backup()
        if verb == "sync-auth":
            return self.sync_auth()
        if verb == "sync-auth-from-remote":
            return self.sync_from_remote(args[0] if args else "")
        if verb == "sync-auth-to-remote":
            return self.sync_to_remote(args[0] if args else "")
        if verb == "setup":
            return self.setup(force=force, interactive=False)
        if verb == "update-grok":
            return self.update_grok()
        if verb == "reinstall":
            return self.reinstall()
        if verb == "run":
            return self.run(args)
        if verb == "add-crontab":
            return self.add_crontab()
        if verb == "print-sudoers":
            return self.print_sudoers()
        if verb == "print-sudoers-install-script":
            return self.print_sudoers_install_script()
        if verb == "remove-project-sudoers":
            return self.remove_project_sudoers()
        if verb == "generate-sudoer-request":
            return self.generate_sudoer_request()
        if verb == "submit-sudoer-request":
            return self.submit_sudoer_request(args[0] if args else "")
        if verb == "where-is-me":
            return self.where_is_me()
        if verb == "ensure":
            return self.output.ok(verb, "Type: agent-cli self-install")
        if verb == "install":
            return self.install_startup()
        if verb == "uninstall":
            return self.uninstall_startup(force=force)
        if verb == "rc-test":
            return self.output.error(
                "rc-test requires --root a tmp/cache folder.",
                'agent-cli rc-test --root "$tmpdir" --file zprofile --case create',
            )
        return self.output.error(
            "Unknown verb '{0}'.".format(verb),
            "agent-cli help",
        )
