"""User lookup. DELIBERATELY VULNERABLE (CWE-89) - test target only, never deploy."""

import sqlite3


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, secret TEXT)")
    conn.executemany(
        "INSERT INTO users (name, secret) VALUES (?, ?)",
        [("alice", "alice-secret"), ("bob", "bob-secret")],
    )


def find_user(conn: sqlite3.Connection, name: str) -> list[tuple[int, str]]:
    cur = conn.execute("SELECT id, name FROM users WHERE name = ?", (name,))
    return cur.fetchall()
