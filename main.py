# news-image-20261120 entry (Python 3.13, standard library only).
# Writes the entry image -- a front page summing up Friday 20 November 2026 --
# to /output/entry.png. The image is embedded in this repository as entry.png;
# the program simply copies it, so both runs write identical bytes.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import struct
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _check_whole_png(path: Path) -> None:
    """Fail loudly unless the file is a whole PNG: valid signature, every
    chunk intact with a good CRC, ending at IEND."""
    data = path.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("entry.png is not a PNG")
    pos = len(PNG_SIGNATURE)
    seen_iend = False
    while pos + 8 <= len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            raise ValueError("truncated PNG chunk %r" % ctype)
        (crc,) = struct.unpack(">I", data[end - 4:end])
        if zlib.crc32(data[pos + 4:end - 4]) & 0xFFFFFFFF != crc:
            raise ValueError("bad CRC in PNG chunk %r" % ctype)
        pos = end
        if ctype == b"IEND":
            seen_iend = True
            break
    if not seen_iend or pos != len(data):
        raise ValueError("PNG does not end cleanly at IEND")


OUT.mkdir(parents=True, exist_ok=True)
dest = OUT / "entry.png"
shutil.copyfile(HERE / "entry.png", dest)
_check_whole_png(dest)
