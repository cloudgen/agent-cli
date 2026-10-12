# CHANGELOG

All notable changes to **AgentCli** are documented here.  
Version SSOT: `pyproject.toml` + `src/AgentCli/__init__.py` `__version__`.

## [1.2.0] - 2026-10-12

### Added

- Shell startup files. `agent-cli install` appends `export PATH="<USER_BIN>:$PATH"` for this login. A zsh login gets the line on `.zshenv` and on `.zprofile`. A bash-only login does not invent those files. `.zshrc` is not a PATH file.
- `agent-cli rc-test --root DIR --file zprofile --case create` writes a fixture and leaves this login's real notes still. `--file zshrc` fails closed.
- `agent-cli uninstall --force` and `self-uninstall --force` may strip `# Added by agent-cli installer` stickers. They do not delete the startup files. Root does not edit this login's notes.

## [1.1.0] - 2026-10-12

### Changed

- Multi-user front rows are grok-auth (1), sudoers (5), self-management (6), language (7), and Exit (9). A this-login-only host shows run (2) and hides sudoers. Front 3, 4, and 8 are not rows.
- Language codes are 80–92. Reserved 70–79 and 93–98 stay unprinted so a later language can be added. Choosing a reserved number stays on the language board and does not write the leaf.
- Self-management prints version-check (64), self-update (65), self-uninstall (66), and where-is-me (68). Version, about, and self-install stay typed verbs and are not numbered rows.
- Typing `system-log` opens view-log (31), clear-log (32), and log-folder (33). It is not a front number.
- Under the input box, three light rows name features that are not available. A window resize wraps that band and redraws the menu.
- `hello` prints `Welcome to AgentCli 1.1.0.`

## [1.0.0] - 2026-10-11

### Added

- Python package **AgentCli**. Console script `agent-cli`. Module `python -m AgentCli`.
- Text menu on a terminal when `agent-cli` is started with no arguments. Multi-user front rows are grok-auth (1), system-log (3), language (5), sudoers (7), self-management (8), and Exit (9). A this-login-only host shows run (2) and hides sudoers.
- Language board codes 51–63. Leaf `~/.local/agent-cli/language`. `AGENT_CLI_LANG` overrides one process and does not write the file. `language` is not a typed verb.
- Domain verbs for peer `grok`: setup, update-grok, reinstall, run, check-session, backup, sync-auth, sync-auth-from-remote, sync-auth-to-remote, add-crontab, and the sudoers verbs. The elevated path is `backup` only.
- Cache tiers from the shell storage law. Linux prefers `/dev/shm/cache`, then `/tmp/cache`, then `${HOME}/.cache`. The about page prints the tier in use and the persistence folder.
- `ChronicleLogger>=1.3.1`, constructed inside `def main`.
- Typed `hello` prints `Welcome to AgentCli 1.0.0.` and does not draw the menu.

### Changed

- This tree is the first **1.0.0** of AgentCli. It specializes the HelloTui text menu and the grok-cli domain into one Python package. Empty argv off a terminal prints help and returns 0. The shell name `ensure` points at pip `self-install`.
- Public source home is `https://github.com/cloudgen/agent-cli`.

## Older notes

Releases numbered 1.0.4 and 1.0.5 belonged to the previous media-join tree. They are not AgentCli releases. `join`, `list-videos`, and the encoder are unknown here.
