#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is one sentence pitching a bizarre startup idea: ridiculous at
first glance, a real business by the second. Same output on every run.
"""
from pathlib import Path
import os

PITCH = "We rent out office plants as emotional support coworkers — they never interrupt, they photosynthesize your stress, and they only ask for water."
# One sentence, 143 characters, written for this bounty only.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")

if __name__ == "__main__":
    main()
