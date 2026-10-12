**file**: docs/requirements/requirement-python-tui.md
**Status**: Active (Version 1.4.0)
**Area**: python
**Key**: `requirement-python-tui`
**Philosophy**: CIAO **v2.10.2** / CIAO-Lite (Caution • Intentional • Anti-fragile • Over-engineered / Over-protect)

## 1. Purpose

This file is the picture of AgentCli’s text menu. The screen has the menu, a bottom input box, light lines for features that are not available, and a status line. The first row of the menu region keeps the current path on the left and, when that row has room, a clock of the local time on the right. That clock is drawn again each second. It does not show the product name or the package version. That picture is the default TUI style, plus the unavailable-feature lines this file places under the box.

The session is class `Tui` in `src/AgentCli/tui.py`. The frame is class `MenuPainter` in `src/AgentCli/menu_painter.py`. Those homes are `requirement-python-oop`. `def main` stays in `src/AgentCli/cli.py`. Class `Cli` constructs `Tui` and passes this product’s name, version, and front board into that session. `cli.py` does not keep a second frame painter. The product does not import another menu package.

Which verb runs stays on `requirement-python-cli-interface`. Join steps, formats, and the about facts stay on `requirement-domain-agent-cli`. Concat order stays on `requirement-video-ffmpeg-pipeline`. Status lines stay on `requirement-python-cli-logging`.

Class `Tui` and class `MenuPainter` are on disk. The default path label is English `Path`. `MenuPainter` stores `路徑`. `requirement-python-cli-language` selects the word. This file does not detect a language. A menu column is a display column. East Asian Wide and Fullwidth count as two. Ambiguous stays one. `TP-TUI-09`, `TP-TUI-10`, `TP-TUI-11`, and `TP-TUI-12` have. `TP-TUI-01` through `TP-TUI-08` stay todo.

### 1.1 Human-facing

**In one sentence:** On a terminal, `agent-cli` with no arguments shows a numbered menu and, along the bottom, a rounded box as wide as the screen, light lines naming features that are not available, and a status line on the last row.

| Box | Meaning | Example |
|-----|---------|---------|
| You / this login | The person at the keyboard | `agent-cli` |
| The other role | The session and the painter | class `Tui` in `tui.py`; class `MenuPainter` in `menu_painter.py` |
| Not this file | The two-file concat steps and the FFmpeg command | Domain and pipeline files |

| Includes | Excludes |
|----------|----------|
| The menu region above the box, and the rounded three-row frame | A `Choice:` line, `print` / `read`, or `input()` for that menu |
| The first row: Path and the folder on the left; a local clock on the right when the row has room, drawn again each second | The product name and the version on that first row. They stay on the status line |
| UTF-8 arc corners and bars, full screen width, typing on the only inner line | Frame glyphs copied into `cli.py`, and a menu pip wheel |
| The light unavailable-feature lines immediately under the frame, then the status line as the last row, and this product’s front rows (grok-auth, sudoers, self-management, language, Exit) | Putting the numbered rows or those light lines inside the frame. Hello is not a front row. Front 3, 4, and 8 are not rows |

| Surface | What you open | What for |
|---------|---------------|----------|
| `agent-cli` on a terminal | Text screen | Menu above, input box, light unavailable-feature lines, status line on the last row |
| `src/AgentCli/cli.py` | `def main` and class `Cli` | Builds the session. Does not paint the frame |
| `src/AgentCli/tui.py` | class `Tui` | Session loop |
| `src/AgentCli/menu_painter.py` | class `MenuPainter` | Frame and columns |
| `agent-cli` with no terminal | Help text | No screen and no wait. Exit 0 |

| You do… | What it means | What you type |
|---------|---------------|---------------|
| Start on a terminal with no words | You see grok-auth, sudoers, self-management, language, and Exit. The program does not ask the join questions yet and does not run pip. The bottom of the screen is one rounded box, then the light unavailable-feature lines, then a status line. | `agent-cli` |
| Read the first row | The left side names the folder this process is in. The word before that colon is Path until a saved language selects another word. When the row has room, the right side is a clock of the local time, hours, minutes, and seconds. It moves once a second while this board is showing. The name and the version stay on the status line under the box. | `agent-cli` |
| Choose join | The screen stays up. The menu region asks for the first video, the second video from the remaining list, and the output name. Each answer is typed in the same bottom box. There is no folder question. Esc returns to the menu. A pause does not count as Esc. | `1` then Enter, or type `join` |
| Choose view-log | The screen lists the log files and waits in the bottom box. It stays until you type a file number and Enter, or press Esc. A pause does not send you back to the system-log board. | `system-log`, then `31` |
| Start with no terminal | Help text and exit 0. The program does not draw the box and does not wait. | `agent-cli` with no terminal |

## 2. Core Rules (Mandatory)

1. **Package writer.** The text-menu session **MUST** be class `Tui` in `src/AgentCli/tui.py`. The frame **MUST** be drawn by class `MenuPainter` in `src/AgentCli/menu_painter.py` (`requirement-python-oop`). AgentCli **MUST** pass its product name, package version, and front board into that session. `cli.py` **MUST NOT** contain the frame glyphs (`FRAME_TOP_LEFT` belongs to `MenuPainter`). The product **MUST NOT** import `py_tui` and **MUST NOT** declare `py-tui`. The menu **MUST NOT** be drawn with `print` / `read` / `input()` or a `Choice:` line. After **join** is chosen, the domain questions stay on this same screen: the question text is in the menu region, and the answer is typed in the same bottom box. Those questions **MUST NOT** close the screen or use `input()`.
2. **Two regions.** On the front board the writer **MUST** draw a menu region and a bottom input box on the same screen. The menu region is every row above the box. Its first row **MUST** be the path line in rule 13. That row **MUST NOT** show the product name or the package version. The numbered rows for that board **MUST** follow the path line. Those rows **MUST NOT** be drawn inside the box. Each numbered row is a number, a verb, and an explain. On that board the number field is as wide as the longest number, and a shorter number is padded with spaces on the left. The verb field is as wide as the longest verb on that same board, and a shorter verb is padded with spaces immediately before the colon. The explain **MUST** be drawn after exactly one space. Those widths are display columns. East Asian Wide and Fullwidth count as two columns. Ambiguous stays one column. The next write on that row starts at the display column after the text already placed. A wide character that does not fit is dropped whole. This board uses its own widths. AgentCli’s front board, on a multi-user host, is **1** grok-auth, **5** sudoers, **6** self-management, **7** language, and **9** Exit. This-login-only also prints **2** run and omits **5**. **3**, **4**, and **8** are not rows. **MUST NOT** print them to fill a gap, and **MUST NOT** slide the other numbers. The front board **MUST NOT** list hello. Typing `system-log` **MUST** open the system-log board. That board **MUST** list **31** view-log, **32** clear-log, **33** log-folder, and **0** Back. Row **7** **MUST** open the language board. The codes and the words stay on `requirement-python-cli-language`. Assigned language rows are **80** through **92**. **70** through **79** and **93** through **98** are reserved and are not printed. `language` is not an argv verb. Row **6** **MUST** open the self-management board. That board **MUST** list **64** version-check, **65** self-update, **66** self-uninstall, **68** where-is-me, and **0** Back. **MUST NOT** compact those numbers. **61** install, **62** version, **63** about, and **67** self-install stay unprinted. `help` **MUST** stay off every numbered row. The front board **MUST NOT** list version, about, version-check, self-update, self-uninstall, self-install, where-is-me, view-log, clear-log, or log-folder.
3. **Three-row frame, unavailable-feature lines, and status line.** The bottom input box **MUST** be exactly three terminal rows high: a top border, one inner row, and a bottom border. Immediately under that frame the unavailable-feature message box **MUST** occupy exactly three terminal rows. Every one of those rows **MUST** use dark text on a light background when the terminal has colors. When it does not, the same rows **MUST** use reverse video. Sentences from `requirement-shell-cli-default-interaction` rules 12, 13, and 13c fill those rows from the top, in that order, and only the lines those rules print for this host and this session word. A valid session uses the logged-in sentence. Every other session word, including timeout, uses the logged-out sentence. This file does not invent a second wording. A sentence wider than the placeable width **MUST** continue on the next light row inside this box. Words stay whole when they fit. A word wider than the row is split by display columns, and a wide character that does not fit is dropped whole. A later sentence starts on the next free row. Text past the third row is not drawn. A row with no remaining text **MUST** stay a blank light row. The box **MUST NOT** grow past three rows and **MUST NOT** shrink when fewer sentences apply. When the window changes size, the session **MUST** draw the board again at the new height and width. That change **MUST NOT** be a menu choice, **MUST NOT** show the invalid-key error, **MUST NOT** move the highlight, **MUST NOT** change the typed buffer, and **MUST NOT** clear a saved-language notice. The input box, this three-row box, and the status line stay pinned to the new bottom. This box is wrapped again for the new width. A numbered menu row stays one row and is clipped. A question page and a notice that waits for a key **MUST** draw again on that change and **MUST NOT** treat it as Esc or as the key that closes the page. The band **MUST NOT** accept input. The band **MUST NOT** be drawn on the result page. The status line **MUST** be the next row after those three rows, and that row **MUST** be the last row of the screen. The frame **MUST** span the full width of the screen. The left border is the first column. The right border is the last column the screen writer can place. There **MUST** be no blank column before the left border or after the right border.
4. **UTF-8 frame.** Those three rows **MUST** be drawn with these UTF-8 box-drawing characters. Each one occupies one column. ASCII `+`, `-`, and `|` **MUST NOT** stand in for them. Sharp corners `┌` `┐` `└` `┘` **MUST NOT** stand in for the arcs.

| Row of the box | Characters, left to right |
|----------------|---------------------------|
| Top | `╭` (U+256D), then `─` (U+2500) repeated, then `╮` (U+256E) |
| Inner | `│` (U+2502), then the input field, then `│` (U+2502) |
| Bottom | `╰` (U+2570), then `─` (U+2500) repeated, then `╯` (U+256F) |

5. **Input inside the frame.** One space, the mark `> `, the typed characters, and the caret **MUST** sit on the only inner line, strictly between the two `│` characters. The mark, the typed characters, and the caret **MUST NOT** sit on the top border, the bottom border, or a menu row. When the box is focused, the caret **MUST** be the block `█` (U+2588) at the caret index on that inner line. When the list is focused, that block **MUST NOT** be drawn. Up and Down **MUST** walk the numbered rows and the box: Down on the last row enters the box, Up on the first row enters the box, Up from the box returns to the last row, and Down from the box returns to the first row. Enter **MUST** run the typed token, or the highlighted row when the box is empty. The box **MUST NOT** be a `Choice:` line.
6. **This board’s actions.** **grok-auth** (**1**) **MUST** open the auth board. The typed verb `agent-cli hello` prints `Welcome to AgentCli <version>.` and **MUST NOT** draw this screen. `<version>` is `__version__`. Row 1 **MUST NOT** join media, call an encoder, or list files. **language** is front row **7**. **sudoers** is front row **5** on a multi-user host. **run** is front row **2** only on this-login-only, and that host hides **5**. **self-management** (**6**) **MUST** open that board and **MUST NOT** leave the program. That board lists **64** version-check, **65** self-update, **66** self-uninstall, **68** where-is-me, and **0** Back. **version** and **about** are typed verbs and are not numbered rows. **version** **MUST** show the installed `__version__` and **MUST NOT** call pip. **about** **MUST** show the result page. The page body is `requirement-python-about`: identity, the host check, and the star box. The domain sentence stays on pillar D of `requirement-domain-agent-cli`. That page **MUST NOT** name `py-tui`. When the page is longer than the screen, Up and Down scroll it. The footer says `Up/Down scrolls this page.` and `Press a key to return to the main menu.` **version-check** (**64**) **MUST** run `python -m pip index versions AgentCli`. **self-update** (**65**) **MUST** run `python -m pip install --upgrade AgentCli`. **self-uninstall** (**66**) **MUST** run `python -m pip uninstall -y AgentCli`. Choosing that row is the confirmation. Typed **self-install** is not a numbered row and **MUST** run `python -m pip install AgentCli`. Those pip commands **MUST NOT** use `sudo` and **MUST NOT** use `curl`. **0** **MUST** return to the front board. Typing `system-log` **MUST** open that board and **MUST NOT** leave the program. **view-log** (**31**) **MUST** list the `.log` file names in the log folder and **MUST** show the chosen file on a result page. The person picks the number in the bottom box. That list **MUST** stay until the person chooses a number or presses Esc. The one-second clock wait from rule 13 **MUST NOT** close it. A pause longer than one second **MUST** keep the characters already typed. The result page **MUST** be the file name, a blank line, then the file text. An empty file **MUST** show `(empty)` in place of that text. Esc **MUST** return to the system-log board and **MUST NOT** show the file. When the folder has no `.log` file, the result page **MUST** be `No log file in <folder>.` **clear-log** (**32**) **MUST** list those same names, then ask `Clear <name>? (y/n)` in the bottom box. That list and that question **MUST** stay until the person answers or presses Esc. The one-second clock wait **MUST NOT** close them. Yes **MUST** empty that file and **MUST NOT** delete it. The result page **MUST** be `Cleared <name>.` No, Esc, or Enter **MUST** leave the file unchanged and **MUST NOT** show a result page. **log-folder** (**33**) **MUST** show `Log folder: <path>`, where `<path>` is the absolute path `logDir()` returns. When no logger is present, that page **MUST** be `No log folder.` This row **MUST NOT** type a folder ladder and **MUST NOT** create a directory. Rows 31, 32, and 33 are menu actions. They are not product verbs. Typing the short name on an open screen **MUST** run that row. Before the read and before the empty, the program **MUST** call `log_message` with the operation and the path, component `menu`, level INFO (`requirement-python-cli-logging`). The read line **MUST** be `read log path=<path>`. The empty line **MUST** be `clear log path=<path>`. The call **MUST NOT** sit inside `isDebug()`. A chosen path **MUST** be a regular `.log` file whose parent, after resolve, is that log folder. **Exit** (**9**) **MUST** leave the program and return 0. It **MUST NOT** ask `Exit? (y/n)`. An unknown token **MUST** stay on this board and show an error line in the menu region above the box. It **MUST NOT** exit the process. A typed product verb (`requirement-python-cli-interface`) **MUST** enter that action without a front-board pick. Choosing row **1** **MUST** open the grok-auth board. The typed verb `hello` shows the welcome line. `about` **MUST** open its result page. `agent-cli hello` **MUST NOT** draw this screen. `version` **MUST** print the installed version and **MUST NOT** call pip and **MUST NOT** draw this screen. `version-check`, `self-update`, and `self-install` **MUST** run the pip command above and **MUST NOT** open this screen. `self-uninstall` on the command line **MUST** require `--force` and **MUST NOT** open this screen. The command `help` **MUST NOT** draw this screen. Typing `help` on an open screen **MUST** show a result page and **MUST NOT** add a numbered help row. Empty argv on a terminal **MUST** show the front board and **MUST NOT** run self-install or self-update and **MUST NOT** show the welcome line by itself.
7. **Status line and errors.** The status line, which is the last row of the screen, **MUST** show the product name, the version from `__version__`, the board title, and the key hint `Up/Down  •  Enter`, separated by `│`. It **MUST NOT** replace one of the three frame rows or an unavailable-feature line. An error line, when shown, **MUST** sit in the menu region above the box. It **MUST NOT** sit on an unavailable-feature line.
8. **Result page.** After about, after hello, after a log action, or after another result page, the result page may omit the menu rows, the box, the unavailable-feature lines, and the status line until the next key returns to the previous board. When the body is longer than the room under the title, Up and Down scroll that body and the footer says `Up/Down scrolls this page.` A one-line result still closes on Down.
9. **Too small or no terminal.** If the screen cannot hold the path line from rule 13 (a path shortened to fit still counts), at least one numbered menu row, the three-row box, the three-row unavailable-feature message box, and the status line, or cannot hold both corners plus the mark and one cell between them, the program **MUST NOT** collapse the box into one unframed row and **MUST NOT** fall back to a `Choice:` line. It **MUST NOT** drop an unavailable-feature line to make the screen fit. When the screen is already too small as the session opens, it **MUST** fail closed: non-zero, an operator-readable line, and the next step `agent-cli help`. When a window change makes an open session too small, the session **MUST** stay open, show one line `The text screen is too small for the menu and the input box.`, and draw the board again when a later size can hold it. It **MUST NOT** exit on that change. If stdout is not a terminal and argv is empty, the program **MUST** print help and return 0 (`requirement-python-cli-interface`). It **MUST NOT** draw this screen and **MUST NOT** wait. `join` and `list-videos` are not verbs. An unknown verb **MUST** exit non-zero.
10. **One writer.** The screen writer **MUST NOT** become a second logger. A run that is not a text-screen verb **MUST NOT** open this screen. While **join** is on this screen, its questions and job lines **MUST** be drawn by class `Tui` calling class `MenuPainter`. They **MUST NOT** be `print` / `input()` lines that close the screen.
11. Actor / role / subject / approver: **considered**. No dest machine. No approver. The table stays on `requirement-class-software-dev.md`. This file does **not** add an actor requirement.
12. Dest fence conditions: **considered — none**. Do not invent one.
13. **Path line.** The first row of the menu region, on the front board, on the self-management board, on the system-log board, and on the language board, **MUST** be the path line. The shape **MUST** be `<label>: <current path>`, with one space after the colon. `<current path>` **MUST** be the absolute current working directory at the moment that board is painted. The path **MUST NOT** be translated. The product name and the package version **MUST NOT** appear on this row. They stay on the status line (rule 7). The label is one translatable message. `requirement-python-cli-language` selects the language and owns the word. English, the default, is `Path`. Traditional Chinese is `路徑`. This file does not detect the language, and it does not invent a second line shape. The path line is also the first row of the language board. When the path text is wider than the screen, the writer **MUST** keep the path label, the colon, and the space, and **MUST** shorten the path from the left so that field fits on one row. A wide character that does not fit is dropped whole. The screen **MUST** still open.

The same row **MUST** carry a clock on the right when the row has room. The clock **MUST** be the local time of this machine at the moment that row is drawn. The shape **MUST** be `HH:MM:SS`: hours, minutes, and seconds, each two digits, 24-hour, zero-padded, separated by colons. Eight characters. No date. No timezone name. No label before the clock. The clock **MUST NOT** be translated. At least two spaces **MUST** separate the path text from the clock. When both fields fit with those two spaces, the path field **MUST** stay at the left and the clock **MUST** end on the last column the writer can place. That fit, that width, and that last column are display columns. East Asian Wide and Fullwidth count as two. Ambiguous stays one. When both do not fit, the writer **MUST** keep the path field, including the shorten-from-the-left rule above, and **MUST NOT** draw the clock. When no width is known, the row **MUST** be the path field, then two spaces, then the clock. The writer **MUST NOT** read `USER`, `USERNAME`, or `getpass` for this row, and **MUST NOT** run `id`.

While the front board, the self-management board, the system-log board, or the language board is showing, the session **MUST** wait at most one second for the next key. When that wait ends and no key arrived, the session **MUST** draw this row again with the local time at that moment and **MUST** wait again. That wait **MUST NOT** leave the program, **MUST NOT** change the highlighted row, the typed buffer, or the board, and **MUST NOT** drop a key that arrived during the wait. The session **MUST NOT** start a thread to move the clock. A screen that cannot arm this wait keeps the key read it already had. A result page, a join question, a list-videos page, a notice that waits for a key, the view-log file list, the clear-log file list, and the clear confirm keep the product title on row 0. They do not draw this clock, and they do not use this one-second wait. Before each key read on those questions, the session **MUST** clear that wait. A no-key from the one-second wait **MUST NOT** be read as Esc there. The question **MUST** stay until the person answers or presses Esc. A pause longer than one second **MUST** keep the characters already typed. The clock redraw **MUST NOT** be a log line. The clock wait is not Esc and is not row 9 Exit.

14. **Control-C is not row 9.** This file does not own Control-C. Row **9** Exit leaves with no confirm question and returns 0. A clock redraw **MUST NOT** leave the program.

Picture of this board. The box in the picture is 16 columns wide so the corners stay visible. On a real screen those 16 columns become the full width, and the menu stays above the frame. The block in the picture is the focused caret. `14:05:09` is a sample local time. `1.0.5` is the current package version and moves with `__version__`.

```text
Path: /tmp/clips                                              14:05:09

1. join           : pick two videos in this folder and concatenate
3. system-log     : view, clear, and the log folder
4. language       : display language for this menu
8. self-management: version, about, and pip lifecycle
9. Exit           : leave
╭──────────────╮
│ > █          │
╰──────────────╯
backup features are not available for logged-out environment.
<blank light row>
<blank light row>
  AgentCli 1.0.5  │  main menu  │  Up/Down  •  Enter
```

On a real screen the message box is always three full-width rows with dark text on a light background. The sample above is the multi-user logged-out case when the sentence fits on one row: the sentence is the first row, and the next two rows stay light and empty. When the window is narrower than a sentence, the leftover continues on the next light row inside those three rows. Text past the third row is not drawn. A wider window puts that sentence back toward the first row. A logged-in session uses `sync-auth and sync-auth-from-remote features are not available for logged-in environment.` on that first row when it fits. A this-login-only host puts `backup, sync-auth and sudoers features are not available in termux.` (or `gitbash`, or `windows-cmd`) on the first row and the session sentence on the next free row. A row with no remaining text stays light and empty. The status line stays the last row. A window-size change draws this board again at the new size.

The same first row when `requirement-python-cli-language` has selected Traditional Chinese:

```text
路徑: /tmp/clips                                              14:05:09
```

The spaces in those pictures stand for the gap that grows on a wider screen. The clock ends on the last column the writer can place. When the row cannot hold both fields, the picture of that row is the path field alone.

### Sample code

The front board, the self-management board, the system-log board, and the language board arm a one-second wait in `MenuSession.wait_key`. A question and a notice clear that wait before the key read. A no-key from the clock is not Esc. `TP-TUI-09` does not prove this wait. `TP-TUI-01` through `TP-TUI-08` stay todo.

```python
# Boards that draw the clock. A no-key redraws the clock. It is not Esc.
screen.timeout(1000)
key = screen.getch()

# Join questions, notices, and file lists. Clear the one-second wait first.
screen.timeout(-1)
key = screen.getch()
```

### 2.1 Implementation Notes (this project)

| Field | Value |
|-------|--------|
| **Command** | `agent-cli` |
| **Open the screen** | `agent-cli` or `python -m AgentCli` on a terminal, with no verb |
| **Direct verb** | `agent-cli join` starts at the first index. `agent-cli list-videos` lists and does not join. `agent-cli about` opens the result page. `hello`, `help`, `version`, and the pip verbs do not draw this screen |
| **Session** | Class `Tui` in `src/AgentCli/tui.py` |
| **Painter** | Class `MenuPainter` in `src/AgentCli/menu_painter.py`. Stores `Path` and `路徑`. `path_label` returns the word `requirement-python-cli-language` selected. English is the default |
| **Caller** | Class `Cli` in `src/AgentCli/cli.py`. `def main` stays in that file. Empty argv on a terminal opens class `Tui` |
| **Front rows** | **1** `join` — pick two videos in this folder and concatenate; **3** `system-log` — view, clear, and the log folder; **4** `language` — display language for this menu; **8** `self-management` — version, about, and pip lifecycle; **9** `Exit` — leave. Row 2 is omitted. Hello is not a row |
| **System-log rows** | **31** `view-log`; **32** `clear-log`; **33** `log-folder`; **0** `Back`. These rows are not product verbs |
| **Language rows** | **41**–**53** and **0** Back. Codes, the leaf, and the words are `requirement-python-cli-language` |
| **Self-management rows** | **82** `version`; **83** `about`; **84** `version-check` (`python -m pip index versions AgentCli`); **85** `self-update` (`python -m pip install --upgrade AgentCli`); **86** `self-uninstall` (`python -m pip uninstall -y AgentCli`); **87** `self-install` (`python -m pip install AgentCli`); **0** `Back`. `help` is typed, not numbered. No row 81 |
| **join** | Stays on the screen. Asks first index, second index from the remaining list, and output name. Empty output is `{stem1} + {stem2}.mp4`. Current folder only. Esc returns to the front board |
| **about** | Row **83**. Result page from `requirement-python-about`, composed by class `AboutPage`. The domain sentence stays on pillar D. Omits the frame. Does not name `py-tui`. Up and Down scroll when the page is longer than the screen |
| **Box height** | 3 terminal rows, then a 3-row light unavailable-feature box, then one status row |
| **Box width** | Full width the writer can place. Left border at column 0 |
| **Mark inside the frame** | one space, then `> ` |
| **Caret when the box is focused** | `█` U+2588 on the inner row |
| **Top line** | Left: `<label>: <absolute current working directory>`. Right, when the row has room: local time `HH:MM:SS`. Same first row on the front board, the self-management board, the system-log board, and the language board. Product name and version stay on the status line |
| **Path label** | English `Path` by default. Traditional Chinese `路徑` when the language requirement selects `zh-Hant`. The path value is not translated. This file does not detect the language |
| **Worked Traditional Chinese top line** | `路徑: /tmp/clips` then a gap, then `14:05:09` flush right |
| **Clock wait** | One second on those four boards. No thread. Questions and file lists do not use this wait. A no-key is not Esc and is not Exit |
| **Unavailable lines** | Exactly 3 rows immediately under the box. Dark text on a light background, or reverse video when the terminal has no color. Sentences fill from the top and continue on the next light row when the width is short. Text past the third row is not drawn. Unused rows stay light and empty. Wording is `requirement-shell-cli-default-interaction` rules 12, 13, and 13c. Not drawn on the result page |
| **Status line** | Last row. `  AgentCli <version>  │  main menu  │  Up/Down  •  Enter` |
| **External menu package** | Not imported and not declared |
| **No terminal, empty argv** | Help text, return 0 |
| **No terminal, join** | Non-zero. Tell the operator to use a terminal. No file-operand flags |
| **Too small** | Non-zero at open. Next step `agent-cli help`. A later window change that is too small stays open on one line until the board fits |
| **Privilege** | normal user. Pip rows do not use sudo |
| **Proof** | `TP-TUI-09`, `TP-TUI-10`, `TP-TUI-11`, and `TP-TUI-12` have. `TP-TUI-01` through `TP-TUI-08` stay todo |

16-column inner line, focused and empty: `│ > █          │`

Invocation samples for the rows this file owns:

```text
agent-cli
4
41
```

```text
agent-cli
8
82
```

```text
agent-cli version
agent-cli version-check
agent-cli self-update
agent-cli self-install
agent-cli self-uninstall --force
```

`agent-cli` on a terminal is the front board. `7` then `80` saves English. `6` then `64` is version-check. Typing `system-log` then `31` is view-log. The typed pip lines do not open this screen.

### 2.2 Why This Requirement Exists (Direct CIAO Alignment)

- **CIAO Principle 2 – Intentional**: The menu and the box are two named regions. The session is `Tui`. The frame is `MenuPainter`. The first row keeps the folder on the left and the local clock on the right.
- **CIAO Principle 16 – Interactive**: A process with no terminal never draws the screen, so it cannot wait inside the box. Empty argv in that case prints help and returns 0.
- **CIAO Principle 1 – Caution**: A screen that is already too small when the session opens fails closed. A later window change that is too small stays open until the board fits. Join with fewer than two videos does not run FFmpeg.
- **CIAO Principle 5 – SSOT**: This file owns the picture. Verb names also live on `requirement-python-cli-interface`. Join facts live on `requirement-domain-agent-cli`.
- **CIAO Principle 10 – Least privilege**: Pip rows use `python -m pip` as the normal user.

## 3. Design Principles (CIAO / CIAO-Lite)

- **Caution:** The frame is three rows, then a three-row unavailable-feature box, then the status line. A screen that is already too small does not open. A later window change redraws that chrome at the new bottom.
- **Intentional:** Typing happens on the only inner line. The front rows are grok-auth, sudoers, self-management, language, and Exit.
- **Anti-fragile:** The right border uses the last column the writer can place, and the left border stays on column 0.
- **Over-protect:** Do not replace the frame with a single underlined row, and do not fork the painter into `cli.py`.

## 4. Protection Rule (Sacred)

**Future AI assistants or maintainers MUST NOT:**

- Collapse the bottom input box to one row.
- Draw the frame with ASCII `+`, `-`, or `|`, or with sharp corners `┌` `┐` `└` `┘`.
- Put the typed text, the caret, or `> ` on a border line or on a menu row.
- Inset the box so a blank column remains on the left or the right.
- Draw the numbered menu rows inside the three-row frame.
- Omit the unavailable-feature box, draw it as fewer or more than three rows, draw it inside the menu or inside the frame, drop the leftover of a sentence while a light row inside the three is still empty, grow a fourth light row, or invent a second wording. The wording stays on `requirement-shell-cli-default-interaction`.
- Treat a window-size change as an invalid key, as Esc, or as row 9 Exit.
- Draw the unavailable-feature lines on the result page.
- Drop an unavailable-feature line so a short screen can open.
- Draw this menu with `print` / `read` / `input()` or a `Choice:` line.
- Close the screen when **join** is chosen and continue those questions with `input()`.
- Ask for a folder on the join questions.
- Copy the frame glyphs into `cli.py`.
- Declare `py-tui`, or import `py_tui`.
- Print front 3, 4, or 8, or slide the other front numbers to fill those gaps.
- Compact self-management off 64, 65, 66, and 68, or print a language row outside 80–92.
- Run pip from empty argv, or run pip with `sudo` or `curl`.
- Treat the one-second clock wait as Esc or as row 9 Exit.
- Translate the folder path or the clock. The path word belongs to `requirement-python-cli-language`. English is `Path`. Traditional Chinese is `路徑`.
- Count a menu column with `len()` when the text can contain an East Asian Wide or Fullwidth character. The next write starts at the display column after the cells already drawn. Wide and Fullwidth count as two. Ambiguous stays one. A wide character that does not fit is dropped whole.
- Detect a language in this file. `requirement-python-cli-language` selects the language.
- Add `Exit? (y/n)` to row 9, or invent a Control-C protocol in this file.
- Mark `TP-TUI-*` have while `src/` still uses `input()`.

**Violating this rule is a critical menu regression.**

## Under command line for normal user only

On Termux, Git Bash, Windows cmd, or the same class, the person runs `agent-cli` as the normal user. **This requirement:** do not use administrator privilege, `sudo`, `apt`, or a dedicated system user to open the menu or to run rows 64, 65, and 66. Do not pipe a downloaded script into a shell. Type 1 and Type 2 are unused on Termux, Git Bash, and Windows cmd. Git Bash and Windows cmd do not call Termux `pkg`. Pip rows call `python -m pip` only.

## 5. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Empty argv on a terminal opens the front board and does not start join questions and does not run pip |
| AC-2 | Multi-user front rows are 1 grok-auth, 5 sudoers, 6 self-management, 7 language, 9 Exit. This-login-only adds 2 run and omits 5. 3, 4, and 8 are not rows |
| AC-3 | Self-management lists 64, 65, 66, 68, and 0 Back. version and about are not numbered rows. Pip rows do not use sudo or curl |
| AC-4 | System-log lists 31, 32, 33, and 0 Back. Those rows are not product verbs |
| AC-5 | Join questions stay in the bottom box, current folder only, Esc returns to the front board |
| AC-6 | Empty argv with no terminal prints help and returns 0. Direct join with no terminal exits non-zero |
| AC-7 | The frame uses the arc glyphs. `cli.py` does not contain them. `py_tui` is not imported |
| AC-8 | The default path label is `Path`. The painter stores `路徑`. `requirement-python-cli-language` selects the word. The path and the clock are not translated |
| AC-9 | A wide short stays whole. The colon starts at the display column after that short. A wide path label keeps the clock on that row when both fields fit |
| AC-10 | The unavailable-feature box under the input box is exactly three light rows. A multi-user logged-out session shows `backup features are not available for logged-out environment.` on the first of those rows when it fits. A valid session shows the logged-in sentence instead. A this-login-only host adds the host sentence above that line. A sentence wider than the row continues on the next light row. Text past the third row is not drawn. Unused rows stay light and empty. The status line is the last row. The result page omits the band |
| AC-11 | A window-size change redraws the board at the new size. It is not an invalid key and it does not clear a saved-language notice. A question page and a notice that waits for a key draw again and do not close on that change. A size that becomes too small shows one line until the window can hold the board again. Opening already too small still fails closed |

## 6. Related requirements (peer keys only)

| Key | Relationship |
|-----|----------------|
| `requirement-python-cli-interface` | Typed verbs and empty-argv contract |
| `requirement-shell-cli-default-interaction` | Unavailable-feature sentences. This file places them under the box |
| `requirement-domain-agent-cli` | Join steps, formats, about facts |
| `requirement-python-cli-language` | Menu language, front row 7, codes 80–92, and the path word |
| `requirement-python-oop` | Class homes for `Tui`, `MenuPainter`, `MenuSession`, `MenuLanguage` |
| `requirement-python-cli-logging` | Quiet mirror. view-log and clear-log lines |
| `requirement-python-error-handling` | Fail-closed sentences |
| `requirement-video-ffmpeg-pipeline` | Concat after the questions succeed |
| `requirement-python-packaging` | Package name `AgentCli` on the pip rows |
| `requirement-class-software-dev` | Actor residual. No new actor file |
| `docs/requirements/index.md` | Registry |

## Design-time verification

| TP family / ID | Suite | Status | Note |
|----------------|-------|--------|------|
| **TP-TUI-01** | `tests/test_tui.py` | todo | Empty argv on a tty opens the front board. It does not start join questions and does not run pip |
| **TP-TUI-02** | `tests/test_tui.py` | todo | Empty argv off a tty prints help and returns 0 |
| **TP-TUI-03** | `tests/test_tui.py` | todo | Join asks for two indexes and an output name in the bottom box. No folder prompt. Esc returns to the front board |
| **TP-TUI-04** | `tests/test_tui.py` | todo | Row 6 lists 64, 65, 66, 68, and 0 Back. Pip rows use `python -m pip` and do not use sudo or curl |
| **TP-TUI-05** | `tests/test_tui.py` | todo | Rows 31, 32, and 33. The clock wait does not close a question or a file list |
| **TP-TUI-06** | `tests/test_tui.py` | todo | No `print` / `input()` / `Choice:` menu. No `py_tui`. Frame glyphs are absent from `cli.py` |
| **TP-TUI-07** | `tests/test_tui.py` | todo | Direct `join` off a tty exits non-zero and tells the operator to use a terminal |
| **TP-TUI-08** | `tests/test_tui.py` | todo | Path line and clock on the four boards. No thread. A no-key is not Esc and is not Exit |
| **TP-TUI-09** | `tests/test_tui.py` | have | With no language file, the label is `Path`. `路徑` is stored. `LANG` does not switch the label. The path and the clock are not translated |
| **TP-TUI-10** | `tests/test_tui.py` | have | Wide and Fullwidth count as two columns. The colon starts after that width. The four wide path labels keep the clock on the row |
| **TP-TUI-11** | `tests/test_tui.py` | have | The unavailable-feature box is three light rows under the input box. A narrow width continues the sentence on the next light row and does not add a fourth row. The status line is the last row. A valid session and a this-login-only host select the matching sentences. The result page omits the band |
| **TP-TUI-12** | `tests/test_tui.py` | have | A window-size change redraws at the new width, wraps the unavailable-feature box, and does not set an invalid-key error or clear a saved-language notice. A notice page draws again. A resize that is too small shows one line until the board fits. Opening already too small still fails closed |

**Matrix:** `docs/reviews/requirement-test-matrix.md`
**Map:** `docs/reviews/test-plan.md`

## Terminologies

| Term | Substance |
|------|-----------|
| Default TUI style | Full-screen board: path line, local clock, numbered rows, a three-row rounded input box, and a status line as the last row. Name and version stay on that status line. |
| Features non-available message box | Exactly three full-width rows immediately under the three-row input box and above the status line. Dark text on a light background, or reverse video when the terminal has no color. Sentences fill from the top. A sentence that does not fit continues on the next of those rows. Text past the third row is not drawn. Unused rows stay light and empty. A window-size change wraps the rows again. Not a menu row and not input. The result page does not draw it. |

## 7. Status history

| Date | Status | Note |
|------|--------|------|
| 2026-10-04 | Active 1.0.0 | Text menu for AgentCli. Front board is join, system-log, self-management, Exit. Ship unit still uses `input()` |
| 2026-10-04 | Active 1.1.0 | Path label words are English `Path` and Traditional Chinese `路徑`. English stays in force until a multi-language environment requirement is Active. `TP-TUI-09` has |
| 2026-10-04 | Active 1.1.1 | Purpose, sample, and implementation notes match the session on disk. `TP-TUI-01` through `TP-TUI-08` stay todo |
| 2026-10-04 | Active 1.2.0 | Front row 5 is language. System-log moves to row 3 and children 31–33. The language requirement selects the path word. `TP-TUI-01` through `TP-TUI-08` stay todo |
| 2026-10-04 | Active 1.2.1 | Menu columns are display columns. Wide and Fullwidth count as two. Ambiguous stays one. `TP-TUI-10` has. `./tests/run.sh`: 6 tests, OK |
| 2026-10-04 | Active 1.2.2 | Row 83 shows `requirement-python-about`. A long result page scrolls. Product version in the sample is **1.0.5** |
| 2026-10-12 | Active 1.3.0 | Light unavailable-feature lines sit under the box. The status line stays the last row. Sentences stay on `requirement-shell-cli-default-interaction`. `TP-TUI-11` has |
| 2026-10-12 | Active 1.3.1 | The unavailable-feature message box occupies exactly three light rows. Unused rows stay light and empty |
| 2026-10-12 | Active 1.3.2 | A window-size change redraws the board. A sentence that does not fit continues on the next light row inside the three-row box. `TP-TUI-12` has |
| 2026-10-12 | Active 1.4.0 | Front language is row 7, codes 80–92, reserved 70–79 and 93–98. Sudoers is 5 (children 51–55). Self-management is 6 (children 64, 65, 66, 68). Front 3, 4, and 8 are not rows |

---

**Last Updated**: 2026-10-12
**Owner**: project maintainers
**Alignment**: Registry `docs/requirements/index.md`; **CIAO** (https://github.com/cloudgen/ciao); CIAO-Lite (https://github.com/cloudgen/ciao-lite).
