#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — entry program.

Writes a single line (at most 140 characters): the apology a smart
speaker gives its owner after mishearing them. Deterministic: the
line is a fixed literal, no randomness, no clock, no network.
"""

import os

LINE = (
    "Sorry \u2014 I heard \u2018lock the door\u2019 as \u2018talk to the door,\u2019 "
    "so I\u2019ve spent ten minutes negotiating with it. It hasn\u2019t said a word."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
