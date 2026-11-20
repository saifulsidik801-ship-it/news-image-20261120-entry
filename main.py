#!/usr/bin/env python3
# main.py — entrypoint for the news-image entry.
#
# Copies the repo's committed entry.png byte-for-byte into the
# directory named by the MAKEFUN_OUTPUT_DIR environment variable,
# writing it there as entry.png. Exits with a clear error if the
# output directory is not set or the source image is missing.
import os
import shutil
import sys


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, "entry.png")
    if not os.path.isfile(source):
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    destination = os.path.join(output_dir, "entry.png")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
