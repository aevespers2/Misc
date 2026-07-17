from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .isolation import DryRunSwitchAdapter


class IsolationRequest(BaseModel):
    device: str
    port: str


def create_app(state_dir: Path) -> FastAPI:
    app = FastAPI(title="PhantomBlock", version="0.1.0")
    adapter = DryRunSwitchAdapter()

    def reports() -> list[dict]:
        items = []
        for path in sorted(state_dir.glob("*.json")):
            try:
                data = json.loads(path.read_text())
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(data, dict) and "host" in data and "status" in data:
                items.append(data)
        return items

    @app.get("/api/reports")
    def list_reports() -> list[dict]:
        return reports()

    @app.get("/api/reports/{host}")
    def get_report(host: str) -> dict:
        for report in reports():
            if report.get("host") == host:
                return report
        raise HTTPException(status_code=404, detail="Host report not found")

    @app.post("/api/isolation/dry-run")
    def isolate(request: IsolationRequest) -> dict:
        return adapter.isolate(request.device, request.port).to_dict()

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        rows = "".join(
            f"<tr><td>{r.get('host','')}</td><td>{r.get('status','')}</td>"
            f"<td>{r.get('collected_at','')}</td><td>{len(r.get('findings',[]))}</td></tr>"
            for r in reports()
        ) or "<tr><td colspan='4'>No reports yet</td></tr>"
        return f"""<!doctype html><html><head><meta charset='utf-8'>
<title>PhantomBlock</title><style>
body{{font-family:system-ui;margin:2rem;max-width:1100px}}table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #bbb;padding:.65rem;text-align:left}}th{{background:#eee}}
code{{background:#eee;padding:.15rem .3rem}}</style></head><body>
<h1>PhantomBlock Fleet Status</h1>
<p>Evidence-first MVP. A finding marked <code>investigate</code> is not proof of compromise.</p>
<table><thead><tr><th>Host</th><th>Status</th><th>Collected</th><th>Findings</th></tr></thead>
<tbody>{rows}</tbody></table></body></html>"""

    return app
