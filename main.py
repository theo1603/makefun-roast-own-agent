#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one line roasting our own make.fun entry-building agent to
/output/entry.txt. Python 3.13, stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "Our agent asked its checklist for permission to be funny; "
    "the checklist is still deliberating and "
    "the deadline left without it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
