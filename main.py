#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.

Writes the pre-rendered meme to /output/entry.png. Stdlib only:
no rendering, no network, no randomness — just a byte copy of
meme.png, which render.py drew at build time with PIL.

The meme, in one glance:
  ME: JUST FIX THE ONE BUG
  -> the robot smugly presses DELETE ALL; its laptop shows
     "$ rm -rf /", "bug fixed", "tests left: 0"
  MY AGENT: DELETED THE BUG, THE TESTS, AND MY JOB.
"""

import os
import shutil

# The meme this program ships, drawn at build time by render.py.
SOURCE = "meme.png"

# The sealed scorer's gate: a whole PNG, at most 1 MiB, at most
# 1024 by 1024 pixels. meme.png is 1024x1024 and well under the cap.
MAX_BYTES = 1048576
WIDTH = 1024
HEIGHT = 1024

ENTRY = "meme.png"


def validate(path):
    """Check the gate rules the sealed scorer enforces: PNG magic,
    1024x1024 dimensions, and under the 1 MiB cap."""
    with open(path, "rb") as f:
        head = f.read(33)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG file"
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    assert (width, height) == (WIDTH, HEIGHT), "meme must be 1024x1024"
    size = os.path.getsize(path)
    assert size <= MAX_BYTES, "meme over the 1 MiB cap"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE)
    validate(src)
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")
    validate("/output/entry.png")
    # The copy must be byte-identical: a truncated write would still
    # be a valid-looking PNG header but a different meme.
    assert os.path.getsize("/output/entry.png") == os.path.getsize(src), \
        "output is not a byte-identical copy of the meme"


if __name__ == "__main__":
    main()
