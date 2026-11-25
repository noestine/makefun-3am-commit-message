#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message, the funniest thing an AI agent would put in
a commit right after breaking production at 3 AM, to /output/entry.txt.

Gate (RULES.txt): the output file must be UTF-8 text of 1-200 characters,
not only whitespace. This program writes exactly one 80-character line,
with no trailing newline, deterministically, using only the standard
library, with no network access and no environment reads.
"""
import os
import sys

DEFAULT_OUTPUT = "/output/entry.txt"

ENTRY = 'fix(prod): rolled back my 3am "improvement" \u2014 confidence was 98%, uptime was not'


def main(argv):
    output = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
