# Regression test for autosp finding f-d842f0e9dabbf9ea7bd3 (job job-dryrun-20261030-1-f-d842f0e9dabbf9ea7bd3).
# Written by autosp's reproduction agent (RED) and verified by autosp's independent
# verifier: it failed on the vulnerable code and passed on the fix
# (patch sha256 af1bbcf147712dc82259614aad7448045e621b53e78c6978b849c23e7bcde8e9; fix PR https://github.com/JA7M1N/autosp-test/pull/5).
# It checks RED's original payload only (PAYLOAD = "' OR '1'='1"). The verifier's payload
# variants (Gate 2) are not part of this test. Report: artifacts/reports/job-dryrun-20261030-1-f-d842f0e9dabbf9ea7bd3.md
import sqlite3
import unittest
from app.db import init_db, find_user

# PAYLOAD demonstrates SQL injection by escaping the string literal or using boolean logic
# e.g., "' OR '1'='1" returns all users instead of just the requested name.
PAYLOAD = "' OR '1'='1"

class TestCWE89SQLInjection(unittest.TestCase):
    def test_find_user_sql_injection(self):
        conn = sqlite3.connect(":memory:")
        init_db(conn)

        # Normal usage works
        alice_results = find_user(conn, "alice")
        self.assertEqual(len(alice_results), 1)
        self.assertEqual(alice_results[0][1], "alice")

        # SQL Injection payload should not bypass parameterization / return all records
        malicious_results = find_user(conn, PAYLOAD)
        # If vulnerable, malicous payload will return all users (2 users in init_db)
        # If securely parameterized, it should return 0 users.
        self.assertEqual(
            len(malicious_results), 
            0, 
            "SQL Injection vulnerability detected: payload bypassed query logic and returned records."
        )

if __name__ == "__main__":
    unittest.main()
