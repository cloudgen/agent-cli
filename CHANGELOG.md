# CHANGELOG

All notable changes to **AgentCli** are documented here.  
Version SSOT: `pyproject.toml` + `src/AgentCli/__init__.py` `__version__`.

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
