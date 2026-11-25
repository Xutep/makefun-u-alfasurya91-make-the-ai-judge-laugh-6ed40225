#!/usr/bin/env python3
"""Entry for make.fun bounty u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic, standard library only: the joke is a fixed string, so every
run produces byte-identical output.
"""

import os

JOKE = "Our office printer has been 'warming up' since Tuesday, which makes it the most committed employee we have."


def output_dir() -> str:
    """Where the grader wants the entry: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    text = JOKE.strip()
    if not text:
        raise ValueError("joke must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
