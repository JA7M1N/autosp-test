"""Minimal WSGI front end: GET /users?name=<name>. Test target only."""

import json
import sqlite3
from collections.abc import Callable, Iterable
from urllib.parse import parse_qs

from app.db import find_user, init_db


def make_app() -> Callable[..., Iterable[bytes]]:
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    init_db(conn)

    def app(environ: dict[str, str], start_response: Callable[..., None]) -> Iterable[bytes]:
        query = parse_qs(environ.get("QUERY_STRING", ""))
        name = query.get("name", [""])[0]
        body = json.dumps(find_user(conn, name)).encode()
        start_response("200 OK", [("Content-Type", "application/json")])
        return [body]

    return app


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    make_server("0.0.0.0", 8080, make_app()).serve_forever()
