# MCP stack (injected — no new Codespace required)

Pull this tree into an **existing** Codespace:

```bash
cd /workspaces/<existing-codespace-repo>
git remote add mcp-stack https://github.com/cantgetalonggta-png/mcp-stack-deploy.git 2>/dev/null || true
# OR if this repo already has mcp-stack/:
git pull origin main
cd mcp-stack/manus-mcp-bridge
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export BRIDGE_TOKEN="${BRIDGE_TOKEN:-$(python -c 'import secrets;print(secrets.token_urlsafe(32))')}"
export MANUS_API_KEY="${MANUS_API_KEY:-}"
python server.py
```

Prefer production URL after Vercel deploy of `manus-mcp-bridge` project.
