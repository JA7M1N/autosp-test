# sqli_app: deliberately vulnerable test target

DO NOT DEPLOY. This app contains an intentional SQL injection (CWE-89) in `app/db.py::find_user`.
It exists only as a reproduction/patching target for autosp and is only ever executed inside the
autosp sandbox (network `none`, read-only workspace).

- Standard library only (sqlite3, wsgiref); no third-party dependencies.
- Functional tests: `python -m unittest discover -s tests -t .` (run from this directory).
