#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (169 characters) to /output/entry.txt.
The sentence is a fixed, authored line: no network, no secrets,
no input files. Everything this entry runs is in this repository.
"""

import os

ENTRY = (
    "I fell asleep in the back seat with my cheek against the cool window, "
    "my father's hand keeping time on the steering wheel to a song I still "
    "hum without knowing its name."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"entry must be 1-280 characters, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the sentence, 169 bytes.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
