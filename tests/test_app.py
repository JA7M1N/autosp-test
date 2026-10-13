import sqlite3
import unittest

from app.db import find_user, init_db


class FindUserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = sqlite3.connect(":memory:")
        init_db(self.conn)

    def test_finds_existing_user(self) -> None:
        self.assertEqual(find_user(self.conn, "alice"), [(1, "alice")])

    def test_unknown_user_returns_nothing(self) -> None:
        self.assertEqual(find_user(self.conn, "mallory"), [])


if __name__ == "__main__":
    unittest.main()
