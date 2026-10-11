#!/bin/sh
# AgentCli test runner. TP-TUI, TP-LANG-01, and TP-DOC-01 do not need a peer grok binary.
set -eu
ROOT="$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}/src${PYTHONPATH:+:$PYTHONPATH}"
python3 -m unittest discover -s tests -v
