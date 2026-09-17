"""Vercel entrypoint.

Only the HTTP surface lives here. kopyya_connector itself is a Tkinter +
headed-Playwright desktop app, so it is deliberately not imported: neither a
display nor a browser exists inside a serverless function.
"""
import os

from fastapi import FastAPI

app = FastAPI(title="Kopyya Connector")

BACKEND_URL = os.environ.get("KOPYYA_BACKEND_URL", "https://kopyya.com")


@app.get("/")
def root() -> dict:
    return {"service": "kopyya-connector", "status": "ok", "backend": BACKEND_URL}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
