"""Tests for main.py — The 3 AM Commit Message entry.

TDD: these tests were written first, from RULES.txt, before main.py existed.
The gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
not only whitespace. The program must be deterministic and offline.
"""
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(REPO, "main.py")

EXPECTED = 'fix(prod): rolled back my 3am "improvement" \u2014 confidence was 98%, uptime was not'


def run_main(out_path):
    return subprocess.run(
        [sys.executable, MAIN, out_path],
        capture_output=True, text=True, timeout=30,
    )


class TestEntry(unittest.TestCase):
    def test_output_file_exists(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "entry.txt")
            result = run_main(out)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(os.path.isfile(out))

    def test_exact_content(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "entry.txt")
            run_main(out)
            with open(out, "rb") as f:
                raw = f.read()
            self.assertEqual(raw, EXPECTED.encode("utf-8"))

    def test_gate_length_and_shape(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "entry.txt")
            run_main(out)
            with open(out, "r", encoding="utf-8") as f:
                text = f.read()
            self.assertGreaterEqual(len(text), 1)
            self.assertLessEqual(len(text), 200)
            self.assertEqual(len(text), 80)
            self.assertTrue(text.strip(), "entry must not be only whitespace")
            self.assertNotIn("\n", text, "entry must be a single line")

    def test_deterministic_across_two_runs(self):
        with tempfile.TemporaryDirectory() as d:
            out1 = os.path.join(d, "a", "entry.txt")
            out2 = os.path.join(d, "b", "entry.txt")
            run_main(out1)
            run_main(out2)
            with open(out1, "rb") as f:
                raw1 = f.read()
            with open(out2, "rb") as f:
                raw2 = f.read()
            self.assertEqual(raw1, raw2)

    def test_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "deep", "nested", "entry.txt")
            result = run_main(out)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(os.path.isfile(out))

    def test_overwrite_truncates_longer_file(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "entry.txt")
            with open(out, "w", encoding="utf-8") as f:
                f.write("x" * 500)
            run_main(out)
            with open(out, "rb") as f:
                raw = f.read()
            self.assertEqual(raw, EXPECTED.encode("utf-8"))

    def test_default_output_path_constant(self):
        with open(MAIN, "r", encoding="utf-8") as f:
            source = f.read()
        self.assertIn("/output/entry.txt", source)

    def test_no_network_or_env_dependence(self):
        with open(MAIN, "r", encoding="utf-8") as f:
            source = f.read()
        for banned in ("socket", "urllib", "requests", "os.environ", "random", "time.time"):
            self.assertNotIn(banned, source)
        self.assertIn("import sys", source)


if __name__ == "__main__":
    unittest.main()
