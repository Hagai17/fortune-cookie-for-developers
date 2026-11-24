#!/usr/bin/env python3
"""Write one fortune-cookie line for a developer to /output/entry.txt.

The line is a single fortune-slip message of at most 120 characters,
written for a software developer: fortune-cookie wisdom about the daily
truths of the work — bugs, reviews, deploys, estimates, legacy code —
with a quiet twist that rewards a second read. The final line was
picked by drafting a slate of candidates and duelling them pairwise on
the bounty judge's criteria — fortune-cookie wisdom first, then the
single-breath balance, how true it rings about a developer's day, the
freshness of its turn, and the double meaning it leaves behind. The
slate and the duels are recorded in candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner (78 characters) — see candidates.md for the full slate.
LINE = (
    "The senior who wrote this code was you, eleven months and "
    "three deadlines ago."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
