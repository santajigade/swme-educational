#!/usr/bin/env python3
"""Write changed.txt listing files changed between two commits (falls back to all files)."""
import subprocess
import sys

before = sys.argv[1] if len(sys.argv) > 1 else ""
after = sys.argv[2] if len(sys.argv) > 2 else "HEAD"


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


out = None
if before and set(before) != {"0"}:
    r = git("diff", "--name-only", before, after)
    if r.returncode == 0:
        out = r.stdout
if out is None:
    out = git("ls-files").stdout

with open("changed.txt", "w", encoding="utf-8") as f:
    f.write(out)
print(out)
