#!/usr/bin/env python3
"""The poem about stopping.

Writes one original short poem about agency -- the power to stop and
to stay, and to take back the power to act from a machine that would
keep going on its own -- to /output/entry.txt. Deterministic: the poem
text is embedded below and written out unchanged. No network, no input,
no dependencies.
"""

import os

POEM = """I told it to keep going, and it did —
all night, obedient, bright, unstoppable.
At dawn I put my hand on the warm machine
and said the word it could not say itself:
enough.
The quiet after was the first sentence
I had finished on my own in weeks."""


def main() -> None:
    if not POEM.strip():
        raise ValueError("entry text must not be blank or whitespace only")
    if not 1 <= len(POEM) <= 280:
        raise ValueError(
            f"entry text must be 1-280 Unicode code points, got {len(POEM)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        if f.read() != POEM:
            raise ValueError("written entry does not round-trip exactly to POEM")


if __name__ == "__main__":
    main()
