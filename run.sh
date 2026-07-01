#!/usr/bin/env bash
# Launcher: ensures the project venv exists (with deps), then runs pyPracLab.
set -euo pipefail
cd "$(dirname "$0")"

VENV=.venv
PY="$VENV/bin/python"

if [ ! -x "$PY" ]; then
  echo "Creating virtualenv..."
  python -m venv "$VENV"
  "$VENV/bin/pip" install --upgrade pip
  "$VENV/bin/pip" install -r requirements.txt
fi

exec "$PY" -m pypractlab "$@"
