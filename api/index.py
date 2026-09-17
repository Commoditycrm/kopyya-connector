"""Vercel entrypoint.

Only the HTTP surface lives here. kopyya_connector itself is a Tkinter +
headed-Playwright desktop app, so it is deliberately not imported: neither a
display nor a browser exists inside a serverless function.
"""
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Kopyya Connector")

BACKEND_URL = os.environ.get("KOPYYA_BACKEND_URL", "https://kopyya.com")
DOWNLOAD_PAGE = (Path(__file__).parent / "download.html").read_text(encoding="utf-8")


@app.get("/", response_class=HTMLResponse)
def root() -> str:
    return DOWNLOAD_PAGE


@app.get("/api/status")
def status() -> dict:
    return {"service": "kopyya-connector", "status": "ok", "backend": BACKEND_URL}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
