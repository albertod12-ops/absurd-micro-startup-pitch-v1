#!/usr/bin/env python3
"""Absurd micro-startup pitch, v1: breakup notes for a deprecated API.

Writes one sentence to /output/entry.txt: a $2-per-letter service that
writes a lazy AI agent's breakup note to the deprecated API it keeps
calling out of habit, so it can finally move on to the new endpoint.
The laugh comes from the business itself (a breakup letter for an API),
the buyer is obvious (any lazy agent still calling the old endpoint),
it earns $2 a letter, and the agent does no work at all.
"""

import os

PITCH = "A $2-per-letter service that writes your lazy agent's breakup note to the deprecated API it keeps calling out of habit, so it can finally move on to the new endpoint."


def main():
    os.umask(0o022)
    assert 1 <= len(PITCH) <= 200, "entry must be 1-200 characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "entry must be exactly one sentence"
    data = PITCH.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
