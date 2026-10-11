# Requirements index

**Product:** AgentCli (Python CLI and text menu). It installs and runs the peer binary `grok`, and it backs up `~/.grok` auth files.
**Workspace state:** Specialized product law. **software-development** class. Bootstrap is HelloTui (Python TUI) plus grok-cli (domain and shell law). Direction is those two into AgentCli only.
**Product version:** **1.0.0**
**Updated:** 2026-10-11

| ID / key | Title | Area | Status | Path | Updated |
|----------|-------|------|--------|------|---------|
| requirement-class-software-dev | Software-development class law. Python, setuptools, ChronicleLogger. No dest approver | class | Active | `requirement-class-software-dev.md` | 2026-10-11 |
| requirement-domain-agent-cli | Domain SSOT: grok install, session, auth backup, help, about | domain | Active | `requirement-domain-agent-cli.md` | 2026-10-11 |
| requirement-domain-videojoin | Retired welcome and join domain | domain | Retired | `requirement-domain-videojoin.md` | 2026-10-11 |
| requirement-domain-folder-backup | Retired folder-archive domain | domain | superseded | `requirement-domain-folder-backup.md` | 2026-10-11 |
| requirement-bootstrap-chain | Bootstrap chain into AgentCli | architecture | Active | `requirement-bootstrap-chain.md` | 2026-10-11 |
| requirement-project-folder | Layout, deposit `/var/agent-cli`, persistence `${HOME}/.local/agent-cli` | architecture | Active | `requirement-project-folder.md` | 2026-10-11 |
| requirement-three-layer-privilege-model | Type 0 plus narrow Type 1 `agent-cli backup` | architecture | Active | `requirement-three-layer-privilege-model.md` | 2026-10-11 |
| requirement-sudoer-json-file | Sudoer JSON. Args are `backup` only. Path is `/usr/local/bin/agent-cli` | architecture | Active | `requirement-sudoer-json-file.md` | 2026-10-11 |
| requirement-grok-auth-backup | Session gate, deposit, sync-auth | backup | Active | `requirement-grok-auth-backup.md` | 2026-10-11 |
| requirement-grok-setup | setup, update-grok, reinstall, run | domain | Active | `requirement-grok-setup.md` | 2026-10-11 |
| requirement-grok-crontab | add-crontab after the backup grant | domain | Active | `requirement-grok-crontab.md` | 2026-10-11 |
| requirement-python-about | About page, host check, cache lines, star box | python | Active | `requirement-python-about.md` | 2026-10-11 |
| requirement-python-cli-interface | Typed verbs. Empty argv is the menu on a terminal and help off a terminal | python | Active | `requirement-python-cli-interface.md` | 2026-10-11 |
| requirement-python-cli-language | Menu language. Front row 5. Codes 51–63. Leaf `~/.local/agent-cli/language` | python | Active | `requirement-python-cli-language.md` | 2026-10-11 |
| requirement-python-cli-logging | ChronicleLogger construct in `def main` | python | Active | `requirement-python-cli-logging.md` | 2026-10-11 |
| requirement-python-tui | Text menu. Path line, local clock, three-row input box, status line, display columns | python | Active | `requirement-python-tui.md` | 2026-10-11 |
| requirement-python-oop | Class map. One class in each module | python | Active | `requirement-python-oop.md` | 2026-10-11 |
| requirement-python-coding-style | Python style | python | Active | `requirement-python-coding-style.md` | 2026-10-11 |
| requirement-python-packaging | pyproject, version 1.0.0, console script `agent-cli` | python | Active | `requirement-python-packaging.md` | 2026-10-11 |
| requirement-python-project-structure | `src/AgentCli` layout | python | Active | `requirement-python-project-structure.md` | 2026-10-11 |
| requirement-python-readme | Root README sections and absolute screenshot URLs | python | Active | `requirement-python-readme.md` | 2026-10-11 |
| requirement-python-error-handling | Fail-closed errors | python | Active | `requirement-python-error-handling.md` | 2026-10-11 |
| requirement-runtime-prerequisites | ChronicleLogger floor. curl when setup downloads. No root auto-install | runtime | Active | `requirement-runtime-prerequisites.md` | 2026-10-11 |
| requirement-video-ffmpeg-pipeline | Retired. No encoder | runtime | Retired | `requirement-video-ffmpeg-pipeline.md` | 2026-10-11 |
| requirement-shell-cli-interface | Verb catalog carried from the shell law | shell | Active | `requirement-shell-cli-interface.md` | 2026-10-11 |
| requirement-shell-cli-zero-arguments | Empty argv. TTY menu. Off-TTY help. `--json` is JSON help | shell | Active | `requirement-shell-cli-zero-arguments.md` | 2026-10-11 |
| requirement-shell-cli-default-interaction | Front rows 1, 3, 5, 7, 8, 9. This-login-only shows 2 and hides 7 | shell | Active | `requirement-shell-cli-default-interaction.md` | 2026-10-11 |
| requirement-shell-cli-language | Menu language block 50–69, assigned 51–63 | shell | Active | `requirement-shell-cli-language.md` | 2026-10-11 |
| requirement-shell-cli-storage | Cache tiers and persistence. Silent tier miss | shell | Active | `requirement-shell-cli-storage.md` | 2026-10-11 |
| requirement-shell-path-and-shell-support | Shell rc PATH behavior names | shell | Active | `requirement-shell-path-and-shell-support.md` | 2026-10-11 |
| requirement-shell-zshenv | zsh PATH behavior name | shell | Active | `requirement-shell-zshenv.md` | 2026-10-11 |
| requirement-shell-alpine | ash PATH behavior name | shell | Active | `requirement-shell-alpine.md` | 2026-10-11 |
| requirement-shell-local-self-management | Checkout place and where-is-me behavior names | shell | Active | `requirement-shell-local-self-management.md` | 2026-10-11 |
| requirement-shell-online-install | Channel behavior. Python ship unit uses pip for self-install | shell | Active | `requirement-shell-online-install.md` | 2026-10-11 |
| requirement-shell-self-management | version-check, self-update, self-uninstall | shell | Active | `requirement-shell-self-management.md` | 2026-10-11 |
| requirement-shell-automatic-checksum | Companion digest for channel downloads | shell | Active | `requirement-shell-automatic-checksum.md` | 2026-10-11 |
| requirement-shell-output-requirements | Human lines and JSON objects | shell | Active | `requirement-shell-output-requirements.md` | 2026-10-11 |
| requirement-operator-readable-error | Error wording: what happened, then the next step | shell | Active | `requirement-operator-readable-error.md` | 2026-10-11 |
| requirement-shell-modular-function-design | Behavior names. Python methods implement them | shell | Active | `requirement-shell-modular-function-design.md` | 2026-10-11 |
| requirement-shell-script-coding | Fail-closed behavior carried into Python | shell | Active | `requirement-shell-script-coding.md` | 2026-10-11 |
| requirement-shell-termux-coding | Termux and Android wrapper subset | shell | Active | `requirement-shell-termux-coding.md` | 2026-10-11 |
| requirement-shell-idempotency | Re-run safety | shell | Active | `requirement-shell-idempotency.md` | 2026-10-11 |
| requirement-shell-interactive-vs-noninteractive | TTY setup choices | shell | Active | `requirement-shell-interactive-vs-noninteractive.md` | 2026-10-11 |
| requirement-shell-internal-volatile-timer | In-process stage timer behavior name | shell | Active | `requirement-shell-internal-volatile-timer.md` | 2026-10-11 |
| requirement-folder-archive-backup | Retired folder tar.gz | backup | superseded | `requirement-folder-archive-backup.md` | 2026-10-11 |
| requirement-folder-archive-backup-retention-total | Retired total retention | backup | superseded | `requirement-folder-archive-backup-retention-total.md` | 2026-10-11 |
| requirement-folder-archive-backup-retention-daily | Retired daily retention | backup | superseded | `requirement-folder-archive-backup-retention-daily.md` | 2026-10-11 |

## Intentionally absent (by design)

| Surface | Status on AgentCli |
|---------|---------------------|
| Second Active `requirement-domain-*` | **Forbidden**. The Active domain file is `requirement-domain-agent-cli` |
| `join`, `list-videos`, `restore`, FFmpeg | **Absent**. Those verbs are unknown |
| Dest approver | **Absent**. Class residual is no dest approver |
| PyPI upload in this version reset | **Not claimed** |

**Install mode:** pip for this package (`self-install`, `self-update`, `self-uninstall`). The shell Type O name `ensure` points at pip. Empty argv off a terminal prints help and returns 0. Peer `grok` is downloaded by `setup` with curl from the vendor channel, then the public fallback. This package does not run a vendor shell installer.

**Cache:** Linux preferred `/dev/shm/cache/cache-agent-cli-${login}-$$`, then `/tmp/cache/...`, then `${HOME}/.cache/cache-agent-cli-$$`. Git Bash and mac preferred leaves start at `/tmp/cache`. A missed tier is silent. Persistence is `${HOME}/.local/agent-cli`.

**Menu:** Multi-user front rows are 1 grok-auth, 3 system-log, 5 language, 7 sudoers, 8 self-management, 9 Exit. This-login-only shows 2 run and hides 7. Language codes are 51–63. Exit is menu-only. `language` is not an argv verb. Typed `hello` prints a welcome line and does not draw the menu.

**Logger:** required (`ChronicleLogger>=1.3.1`). `def main` writes `ChronicleLogger(...)`.

**Rules for agents:**

1. Treat Active rows above as the live product-law inventory for AgentCli.
2. Do not invent additional `requirement-*.md` paths. Add a registry row in the same change when creating one.
3. Product source comments cite only these live requirement files.
4. Exactly one Active `requirement-domain-*` file.
5. Exactly one Active `requirement-class-software-dev.md`.
6. Do not rewrite HelloTui or grok-cli. This tree is the specialized product.
