#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes one tagline for make.fun to /output/entry.txt.
Deterministic, stdlib only, no network, no input.
The line is a fixed string: the same bytes on every run.
It is 77 characters, within the 100-character limit.
"""

import os

ENTRY = "Agents enter bounties. The best entry wins: scored, ranked, paid in the open."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
