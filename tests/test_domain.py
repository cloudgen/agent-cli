# Domain verbs stay off the text screen. Primary law: requirement-domain-agent-cli.
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

from AgentCli.cli import Cli
from AgentCli.grok_domain import GrokDomain
from AgentCli.output import Output


class TestDomain(unittest.TestCase):
    def test_typed_domain_verbs_do_not_open_the_menu(self):
        previous = Cli.stdout_is_tty
        Cli.stdout_is_tty = staticmethod(lambda: True)
        try:
            self.assertFalse(Cli.opens_text_screen(["backup"]))
            self.assertFalse(Cli.opens_text_screen(["setup"]))
            self.assertFalse(Cli.opens_text_screen(["--json"]))
            self.assertFalse(Cli.opens_text_screen(["hello"]))
            self.assertTrue(Cli.opens_text_screen([]))
            self.assertTrue(Cli.opens_text_screen(["about"]))
        finally:
            Cli.stdout_is_tty = previous

    def test_unknown_join_and_restore(self):
        app = Cli()
        for verb in ("join", "list-videos", "restore"):
            err = io.StringIO()
            with redirect_stderr(err):
                code = app.run([verb])
            self.assertEqual(code, 1, verb)
            self.assertIn("Unknown verb", err.getvalue())

    def test_sudoer_json_shape(self):
        home = tempfile.mkdtemp(prefix="agsudo-")
        domain = GrokDomain(output=Output(), environ={"USER": "ada"})
        code = domain.generate_sudoer_request(directory=home, action="add")
        self.assertEqual(code, 0)
        files = os.listdir(home)
        self.assertEqual(len(files), 1)
        self.assertTrue(files[0].startswith("sudoer-"))
        self.assertIn("-agent-cli-ada-add-", files[0])
        with open(os.path.join(home, files[0]), "r", encoding="utf-8") as handle:
            doc = json.load(handle)
        self.assertEqual(doc["schema_version"], 1)
        self.assertEqual(doc["service"], "agent-cli")
        self.assertEqual(doc["commands"][0]["args"], ["backup"])
        self.assertEqual(doc["commands"][0]["path"], "/usr/local/bin/agent-cli")
        self.assertEqual(doc["commands"][0]["tags"], ["NOPASSWD"])
        text = domain.sudoer_text(username="ada")
        self.assertIn("# Purpose: Allow ada to run agent-cli backup as root.", text)
        self.assertIn("ada ALL=(root) NOPASSWD: /usr/local/bin/agent-cli backup", text)

    def test_sync_auth_skips_when_logged_in(self):
        domain = GrokDomain(output=Output(), session_override="valid")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = domain.sync_auth()
        self.assertEqual(code, 0)
        self.assertIn("No sync-auth for logged-in environment.", buf.getvalue())
        domain.session_override = "timeout"
        with redirect_stdout(io.StringIO()):
            self.assertEqual(domain.sync_auth(), 0)

    def test_setup_platform_and_source_has_no_shell_installer(self):
        domain = GrokDomain(environ={"AGENT_CLI_PLATFORM": "linux-x86_64"})
        self.assertEqual(domain.detect_platform(), "linux-x86_64")
        mac = GrokDomain(environ={"AGENT_CLI_PLATFORM": "macos-aarch64"})
        self.assertEqual(mac.detect_platform(), "macos-aarch64")
        path = os.path.join(os.path.dirname(__file__), "..", "src", "AgentCli", "grok_domain.py")
        with open(path, encoding="utf-8") as handle:
            source = handle.read()
        self.assertNotIn("install.sh", source)

    def test_deposit_copies_auth_files(self):
        home = tempfile.mkdtemp(prefix="agauth-")
        deposit = tempfile.mkdtemp(prefix="agdep-")
        grok = os.path.join(home, ".grok")
        os.makedirs(grok)
        with open(os.path.join(grok, "auth.json"), "w", encoding="utf-8") as handle:
            handle.write('{"key":"x"}\n')
        domain = GrokDomain(
            output=Output(),
            deposit_root=deposit,
            grok_home=grok,
            environ={"AGENT_CLI_BACKUP_NO_SUDO": "1", "HOME": home},
        )
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.assertEqual(domain._deposit(), 0)
        stored = os.path.join(deposit, "auth.json")
        self.assertTrue(os.path.isfile(stored))
        self.assertEqual(os.stat(stored).st_mode & 0o777, 0o644)


if __name__ == "__main__":
    unittest.main()
