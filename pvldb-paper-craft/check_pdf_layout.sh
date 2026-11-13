#!/usr/bin/env bash
# Wrapper: prefers a local venv if present, else whatever `python3` has pymupdf.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
if [[ -x "$HERE/../.venv/bin/python" ]]; then
  PY="$HERE/../.venv/bin/python"
elif [[ -x "$HERE/.venv/bin/python" ]]; then
  PY="$HERE/.venv/bin/python"
else
  PY="python3"
fi
exec "$PY" "$HERE/check_pdf_layout.py" "$@"
