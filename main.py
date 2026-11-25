#!/usr/bin/env python3
"""Entry for make.fun bounty u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic, standard library only: the joke is a fixed string, so every
run produces byte-identical output.
"""

import os

JOKE = "Our office printer has been 'warming up' since Tuesday, which makes it the most committed employee we have."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
