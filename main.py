"""Worst Superpower entry: writes one useless-superpower one-liner.

Deterministic, offline, stdlib-only. Writes exactly one line of text
(116 characters) to /output/entry.txt.
"""

import os

ENTRY = (
    "I can predict the future with 100% accuracy, "
    "but only events that already happened, "
    "and only after they've happened."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
