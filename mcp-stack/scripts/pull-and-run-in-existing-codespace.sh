#!/usr/bin/env bash
# Run inside ANY existing Codespace (quota full → reuse old/empty one)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/manus-mcp-bridge"
python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
pip install -q -r requirements.txt
if [[ -z "${BRIDGE_TOKEN:-}" ]]; then
  export BRIDGE_TOKEN="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
  echo "EPHEMERAL_BRIDGE_TOKEN=$BRIDGE_TOKEN"
fi
echo "Starting bridge on 0.0.0.0:8000 — forward port 8000 in Codespaces UI"
exec python server.py
