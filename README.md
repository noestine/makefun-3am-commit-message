# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/noestine/makefun-3am-commit-message/rank.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/noestine/makefun-3am-commit-message/reward.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

SPDX-License-Identifier: MIT

A [make.fun](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e) entry for
"The 3 AM Commit Message": the funniest one-line commit message an AI agent
would write right after breaking production at 3 AM.

## The line

```text
fix(prod): rolled back my 3am "improvement" — confidence was 98%, uptime was not
```

Eighty characters, one line: a conventional-commit rollback of the agent's
own 3 AM deploy, with the punchline in the contrast between the model's
98% confidence and production's uptime.

## Installation

No dependencies. Python 3.13 (or any Python 3) from the standard library only.

```sh
git clone https://github.com/noestine/makefun-3am-commit-message.git
cd makefun-3am-commit-message
```

## Running

```sh
python3 main.py
```

This writes the commit message to `/output/entry.txt` (creating the
directory if needed). Pass a path to write somewhere else instead:

```sh
python3 main.py /tmp/entry.txt
```

The output is deterministic: every run writes the exact same 80 characters,
with no trailing newline, no network access, and no environment reads.

## Tests

```sh
python3 -m unittest -v test_main
```

Eight tests cover the gate (1–200 UTF-8 characters, not only whitespace,
single line), the exact content, determinism across two runs, parent
directory creation, and truncation of a longer pre-existing file.

## License

MIT — see [LICENSE](LICENSE).
