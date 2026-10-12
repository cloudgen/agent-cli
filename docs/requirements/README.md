# Requirements

Authoritative specialized product law for **AgentCli** lives here.

**Current state (2026-10-12):** Specialized **software-development** product. Left genesis. Registry is populated — see `index.md`. Product version is **1.1.0**. Exactly one Active domain file: `requirement-domain-agent-cli`.

## Product identity (summary)

| Field | Value |
|-------|--------|
| Product / package | `AgentCli` |
| Version SSOT | **`1.1.0`** (`pyproject.toml` + `src/AgentCli/__init__.py`) |
| Product README SSOT | Root `README.md`. Sections and pictures: `requirement-python-readme` |
| Ship surface | Python package; console script **`agent-cli`**; module `python -m AgentCli` |
| Install mode | **pip / local package** (`pip install AgentCli`; this tree **1.1.0**; checkout `pip install -e .`). Empty argv off a terminal prints help and returns 0 |
| Domain surface | `requirement-domain-agent-cli` — install and run peer `grok`, and back up `~/.grok` auth files |
| Text menu | `requirement-python-tui` — multi-user front rows 1 grok-auth, 5 sudoers, 6 self-management, 7 language, 9 Exit. This-login-only shows 2 run and hides 5. Front 3, 4, and 8 are not rows |
| Menu language | `requirement-python-cli-language` — row 7, codes 80–92, reserved 70–79 and 93–98, leaf `~/.local/agent-cli/language`. `language` is not an argv verb |
| Status logger | `requirement-python-cli-logging` — `ChronicleLogger(...)` inside `def main`. Required (`ChronicleLogger>=1.3.1`) |
| Cache | `requirement-shell-cli-storage` — Linux preferred `/dev/shm/cache`, then `/tmp/cache`, then `${HOME}/.cache`. Silent tier miss |
| Class map | `requirement-python-oop` — one class in each module under `src/AgentCli/` |
| Encode ops | `requirement-video-ffmpeg-pipeline` — **Retired**. This product does not join media |
| Privilege | `requirement-three-layer-privilege-model` — Type 1 is `agent-cli backup` only |
| Runtime tools | **curl** when `setup` downloads peer `grok`. **ChronicleLogger>=1.3.1** required |

## Class requirement gate

| Class | Required class file |
|-------|---------------------|
| software-development | `requirement-class-software-dev.md` (**Active**) |
| genesis-template | N/A — this workspace is no longer genesis for product law |

## Purpose

- **Plan** designs work by reading and updating these docs.  
- **Implement** delivers code that **traces** to these requirements.  
- **Review** verifies delivery against requirements and CIAO checklists.  
- Product **README** must stay honest with this law (install, features, version).

## Layout

| Path | Role |
|------|------|
| `docs/requirements/index.md` | Registry of all requirements — keep in sync |
| `docs/requirements/requirement-*.md` | CIAO-style project requirements |

## Status values

Typical: `draft` · `Active` · `approved` · `in-progress` · `done` · `deprecated` · `superseded`

## Rules

1. Never invent paths — verify on disk.  
2. Class files only via class process; non-class via create-specific process.  
3. Never dump harness inventories into this versioned surface.  
4. Online shell install and Type 1 elevation stay **absent** unless product mode is explicitly changed.  
5. Sole domain SSOT: `requirement-domain-videojoin.md`.  
6. When changing join/publish behavior: update pipeline + coding-style REQs **and** root `README.md` in the same change.  
7. Version dual SSOT + README Version badge must match when a release is claimed.
