# AgentCli - Install and run xAI grok, and back up its auth files

[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square)](https://github.com/cloudgen/agent-cli)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE.md)
[![CIAO](https://img.shields.io/badge/CIAO-Defensive%20Programming-orange?style=flat-square)](https://github.com/cloudgen/ciao)
[![Stars](https://img.shields.io/github/stars/cloudgen/agent-cli?style=flat-square)](https://github.com/cloudgen/agent-cli)
[![Python](https://img.shields.io/badge/Python-2.7%2B%20(3.x%20recommended)-blue?style=flat-square)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/AgentCli?style=flat-square)](https://pypi.org/project/AgentCli/)

AgentCli installs and runs the peer binary `grok`, and it backs up `~/.grok` auth files. Typed verbs do that work in the terminal. The text menu uses the same tokens. `hello` prints one welcome line and does not draw the menu. **Exit** is menu-only.

## Features

- Console script `agent-cli` and module entry `python -m AgentCli`.
- On a terminal with no arguments, the text menu opens. The first row names the current directory on the left and a local clock (`HH:MM:SS`) on the right when the row has room.
- Multi-user front rows are **1 grok-auth**, **3 system-log**, **5 language**, **7 sudoers**, **8 self-management**, and **9 Exit**. A this-login-only host shows **2 run** and hides **7**.
- **grok-auth** covers session, backup, sync, crontab, setup, and reinstall. **sudoers** covers the backup grant only.
- Thirteen menu languages, codes **51**–**63**. The saved leaf is `~/.local/agent-cli/language`. `AGENT_CLI_LANG` overrides one process and does not write the file. `language` is not a typed verb.
- **about** stays in English. It prints the domain line, the runtime tools, a host check, the cache tiers, and the persistence folder.
- Pip lifecycle: `version-check`, `self-update`, `self-install`, and `self-uninstall`. Those verbs do not use sudo. `self-uninstall` on the command line needs `--force`.
- Empty arguments on a terminal do not run pip and do not download `grok`. With no terminal and no verb, the program prints help and returns 0.

## Advantages

1. **Two ways to do the work.** A menu number and the same typed verb share one action. `agent-cli hello` prints `Welcome to AgentCli 1.0.0.` and does not draw the menu. With no arguments on a terminal, the text menu opens and waits. With no terminal and no verb, the program prints help and returns 0.
2. **Built-in languages.** Row **5** lists thirteen languages. The choice is saved for the next run. Leaf shorts stay English.
3. **Cache and persistence.** Linux prefers `/dev/shm/cache`, then `/tmp/cache`, then a leaf under the home cache directory. A missed tier is silent. Persistence is `~/.local/agent-cli`. The about page names the tier this process selected.
4. **A narrow root path.** The only elevated action is `agent-cli backup`, and only after an administrator installs a sudoers fragment whose argument is `backup`. Other verbs stay this login. Peer `grok` is fetched by `setup` from the vendor channel, then the public fallback. This package does not run a vendor shell installer.

| Feature | Typed verb | Text menu |
|---------|------------|-----------|
| Daily start on a terminal | `agent-cli menu` | empty argv |
| Welcome line | `agent-cli hello` | not a front row |
| Peer binary | `agent-cli setup` | grok-auth row **15** |
| Auth deposit | `agent-cli backup` | grok-auth row **11** when signed in |
| Menu language | not a verb | row **5**, codes **51**–**63** |
| This computer | `agent-cli about` | self-management row **83** |
| Pip lifecycle | `version-check`, `self-update`, `self-install`, `self-uninstall` | rows **84**–**87** and **91**–**93** |

## Quick Installation

**Python:** 2.7 or newer, excluding 3.0 through 3.4. 3.x is recommended.

**Python dependency:** `ChronicleLogger>=1.3.1` (required). Pip installs it with AgentCli. `setup` needs `curl` when it downloads peer `grok`.

```bash
pip install AgentCli
```

This installs the console entry **`agent-cli`** and the package **`AgentCli`**. Packaging name SSOT is `pyproject.toml` `[project].name` = `AgentCli`. This tree is **1.0.0**. The PyPI badge above shows the live index. Nothing in this tree uploads a release by itself.

From a checkout:

```bash
git clone https://github.com/cloudgen/agent-cli.git
cd agent-cli
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

After install, on a terminal, `agent-cli` with no arguments prints this screen. The verb is the short token. The note after the colon is the explanation. `9` leaves. `0` on a submenu goes back. A number that is not on the list prints an error and lets you choose again. The path row is the current directory and a local clock (`HH:MM:SS`).

```text
$ agent-cli
Path: <current directory>                                          HH:MM:SS
1. grok-auth      : session, backup, and setup
3. system-log     : view, clear, and the log folder
5. language       : display language for this menu
7. sudoers        : grant backup as root
8. self-management: version, about, and pip lifecycle
9. Exit           : leave
```

## Usage

```bash
agent-cli
python -m AgentCli
```

**hello** prints the welcome line in the terminal and does not draw the menu:

```bash
agent-cli hello
```

```bash
agent-cli help
agent-cli version
agent-cli about
agent-cli hello
agent-cli setup
agent-cli check-session
agent-cli backup
agent-cli where-is-me
agent-cli version-check
agent-cli self-update
agent-cli self-install
agent-cli self-uninstall --force
```

`version` prints `AgentCli 1.0.0` and does not call pip. `about` shows one English page: the product identity, a host check of this computer, the cache tiers, the persistence folder, and a star box. It does not call pip. `hello` prints `Welcome to AgentCli 1.0.0.` and does not draw the menu. `help` prints usage.

`setup` downloads peer `grok` for this platform and links `~/.grok/bin/grok`. `backup` copies `auth.*` into `/var/agent-cli` when this login may run that one command as root. `sync-auth` copies the deposit back and skips that copy when grok is already signed in. `add-crontab` stays closed until the backup grant is present.

`version-check` runs `python -m pip index versions AgentCli`. `self-update` runs `python -m pip install --upgrade AgentCli`. `self-install` runs `python -m pip install AgentCli`. `self-uninstall` runs `python -m pip uninstall -y AgentCli` and needs `--force` on the command line. Those pip verbs do not use sudo. Empty arguments do not install or update.

```python
from AgentCli import main
main()
```

## Screenshots

Each heading is the file name. The paragraph is what that picture shows. Package **1.0.0**. The path row is the current directory. The clock on these captures is `12:06:45`. Leaf shorts stay English.

### `language-menu.png`

Row **5** has opened the language list. **51 English** is highlighted, with the note "use English for this menu." The other rows are **52 简体中文**, **53 繁體中文**, **54 Español**, **55 العربية**, **56 Français**, **57 Português**, **58 Русский**, **59 Deutsch**, **60 日本語**, **61 한국어**, **62 Nederlands**, and **63 Ελληνικά**. Each note says to use that language for this menu. **0 Back** says "return to the main menu." The path label is `Path`. The local clock is on the right of that row. The status line says `language`.

![Language list, 51 English highlighted](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/language-menu.png)

### `main-menu-en.png`

English main menu. The path label is `Path`. The local clock is on the right of that row. **1 grok-auth** is shown as "session, backup, and setup." Then **3 system-log**, **5 language**, **7 sudoers**, **8 self-management**, and **9 Exit**. The status line says `main menu`.

![English main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-en.png)

### `main-menu-zh-hans.png`

Simplified Chinese main menu. The path label is `路径`. **1 grok-auth** stays the English token. **3** is `系统日志`, **5** is `语言`, **7** stays `sudoers`, **8** is `自我管理`, and **9** is `离开`.

![Simplified Chinese main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-zh-hans.png)

### `main-menu-zh-hant.png`

Traditional Chinese main menu. The path label is `路徑`. **3** is `系統日誌`, **5** is `語言`, **8** is `自我管理`, and **9** is `離開`.

![Traditional Chinese main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-zh-hant.png)

### `main-menu-es.png`

Spanish main menu. The path label is `Ruta`. **3** is `registro`, **5** is `idioma`, **8** is `autogestión`, and **9** is `Salir`.

![Spanish main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-es.png)

### `main-menu-ar.png`

Arabic main menu. The path label is `المسار`. The numbers stay on the left. **3** is `سجل النظام`, **5** is `لغة`, **8** is `إدارة ذاتية`, and **9** is `خروج`.

![Arabic main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-ar.png)

### `main-menu-fr.png`

French main menu. The path label is `Chemin`. **3** is `journal`, **5** is `langue`, **8** is `autogestion`, and **9** is `Quitter`.

![French main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-fr.png)

### `main-menu-pt.png`

Portuguese main menu. The path label is `Caminho`. **3** is `registo`, **5** is `idioma`, **8** is `autogestão`, and **9** is `Sair`.

![Portuguese main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-pt.png)

### `main-menu-ru.png`

Russian main menu. The path label is `Путь`. **3** is `системный журнал`, **5** is `язык`, **8** is `самоуправление`, and **9** is `Выход`.

![Russian main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-ru.png)

### `main-menu-de.png`

German main menu. The path label is `Pfad`. **3** is `Systemprotokoll`, **5** is `Sprache`, **8** is `Selbstverwaltung`, and **9** is `Beenden`.

![German main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-de.png)

### `main-menu-ja.png`

Japanese main menu. The path label is `パス`. **3** is `システムログ`, **5** is `言語`, **8** is `自己管理`, and **9** is `終了`.

![Japanese main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-ja.png)

### `main-menu-ko.png`

Korean main menu. The path label is `경로`. **3** is `시스템 로그`, **5** is `언어`, **8** is `자기관리`, and **9** is `종료`.

![Korean main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-ko.png)

### `main-menu-nl.png`

Dutch main menu. The path label is `Pad`. **3** is `systeemlog`, **5** is `taal`, **8** is `zelfbeheer`, and **9** is `Afsluiten`.

![Dutch main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-nl.png)

### `main-menu-el.png`

Greek main menu. The path label is `Διαδρομή`. **3** is `αρχείο καταγραφής`, **5** is `γλώσσα`, **8** is `αυτοδιαχείριση`, and **9** is `Έξοδος`.

![Greek main menu](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/main-menu-el.png)

### `system-log.png`

Row **3** has opened system-log. **31 view-log** is "list a log file and show it." Then **32 clear-log**, **33 log-folder**, and **0 Back**. The path label is `Path`. The local clock is on the right of that row. The status line says `system-log`.

![System log, 31 view-log](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/system-log.png)

### `self-management.png`

Row **8** has opened self-management. **82 version** is "show the installed version." **83 about** is "version and this computer." **84** and **91** are version-check. **85** and **92** are self-update. **86** and **93** are self-uninstall. **87** is self-install. **94 where-is-me** shows agent-cli and grok. **0 Back** returns to the main menu. The local clock is `12:06:45`.

![Self-management, version and pip lifecycle](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/self-management.png)

### `grok-auth.png`

**1 grok-auth** on a multi-user host while the session word is `missing`. The board shows **12 sync-auth-from-remote**, **13 sync-auth**, **14 add-crontab**, **15 setup**, **16 reinstall**, and **0 Back**. A signed-in session shows **11 backup** instead of the sync rows. The local clock is on the path row.

![Logged-out grok-auth board](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/grok-auth.png)

### `sudoers.png`

Row **7** has opened sudoers. The rows are **1 generate-sudoer-request**, **2 submit-sudoer-request**, **3 print-sudoers**, **4 print-sudoers-install-script**, **5 remove-project-sudoers**, and **0 Back**. The grant argument is `backup` only.

![Sudoers board, backup grant only](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/sudoers.png)

### `tui-about.png`

**about** stays in English. The page prints `AgentCli 1.0.0`, `Domain: Install and run xAI grok, and back up its auth files.`, `Runtime tools: curl, grok`, and `Entry points: agent-cli, python -m AgentCli`. The host check is headed `[CHECK SYSTEM]:` and includes the cache lines: cache folder used, preferred, 1st fallback, 2nd fallback, and persistence storage. There is no input box. The page does not call pip.

![About page with cache lines](https://raw.githubusercontent.com/cloudgen/agent-cli/main/screenshots/tui-about.png)

## Examples

```bash
agent-cli
agent-cli version
agent-cli hello
agent-cli about
agent-cli setup
```

`version` prints `AgentCli 1.0.0` and does not call pip. A run that is not the text menu can also print ChronicleLogger status lines above that. The text menu keeps those lines off the screen.

```bash
agent-cli hello
```

That prints `Welcome to AgentCli 1.0.0.` and does not draw the menu.

## Platform Compatibility

Linux is the primary host. macOS and Windows work when Python is present. `setup` selects `linux`, `macos`, or `windows`, and `x86_64` or `aarch64`. The text menu needs a terminal. Git Bash and Windows cmd are this-login-only: they show **run** and hide **sudoers**. Termux is detected from `TERMUX_VERSION` or `AGENT_CLI_HOST_OVERRIDE=termux`.

## Related Projects

- [AgentCli on GitHub](https://github.com/cloudgen/agent-cli) — this program’s source
- [AgentCli on PyPI](https://pypi.org/project/AgentCli/) — this program on PyPI
- [grok-cli](https://github.com/cloudgen/grok-cli) — shell sibling this Python package specializes beside
- [ChronicleLogger](https://github.com/Wilgat/ChronicleLogger) — status logger this program depends on (`ChronicleLogger>=1.3.1`)
- [CIAO](https://github.com/cloudgen/ciao) — Caution, Intentional, Anti-fragile, Over-engineered
- [CIAO-Lite](https://github.com/cloudgen/ciao-lite) — short agent contract
- [safe-rm](https://github.com/cloudgen/safe-rm) — guarded `rm`

## Contributing

1. Keep product law in `docs/requirements/` aligned with this document when behavior changes.
2. Do not add `join`, `list-videos`, or an encoder. Those verbs stay unknown.
3. Version dual SSOT: bump **`pyproject.toml`** and **`src/AgentCli/__init__.py`** `__version__` together.
4. Do not widen the root path past `agent-cli backup`.
5. Empty argv on a terminal opens the menu. Empty argv off a terminal prints help and returns 0.

## License

MIT. See [LICENSE.md](LICENSE.md).

Copyright (c) 2026 cloudgen.

## Last Update

2026-10-11 — **1.0.0**. The package name is **AgentCli** and the console script is `agent-cli`. The text menu keeps the path line, the local clock (`HH:MM:SS`), the three-row input box, and the status line. Front rows are grok-auth, system-log, language, sudoers, self-management, and Exit. Language codes are **51**–**63**. The about page names the cache tiers. `ChronicleLogger>=1.3.1` is required. Pictures in `screenshots/` match this menu.
