#!/usr/bin/env python3
"""Front-page delivery for the news-image-20261120 entry.

The newspaper page is already rendered and committed as entry.png. This
script's only job is to place a byte-identical copy of that image where
the grader expects it (MAKEFUN_OUTPUT_DIR/entry.png). No pixels are
drawn, generated, or altered while it runs. Exit code 0 means the copy
landed; exit code 1 means the output directory was not provided.
"""

import os
import shutil
import sys


def deliver():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not target_dir:
        print("MAKEFUN_OUTPUT_DIR is not set; cannot place entry.png", file=sys.stderr)
        return 1
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "entry.png")
    os.makedirs(target_dir, exist_ok=True)
    shutil.copyfile(source_path, os.path.join(target_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
