"""One Line, One Chill entry (Python 3.13, standard library only).

Writes one single-sentence horror line to /output/entry.txt.
Gate: UTF-8 text of 1 to 200 characters, not only white space.
The judge reads exactly the bytes written, so the line carries
no trailing newline.

Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "Every night the baby monitor caught a woman singing my daughter "
    "to sleep in my own voice, and last night she sang along."
)

Path(OUTPUT_DIR, "entry.txt").write_text(LINE, encoding="utf-8")
