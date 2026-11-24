"""One Word, First Thought — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the first word that
came to mind. The word is "Petrichor": the smell of rain falling on
dry earth. A single vivid, specific word — a scent everyone knows
but almost no one can name.
"""

import os

WORD = "Petrichor"


def main() -> None:
    assert WORD and not any(c.isspace() for c in WORD), "entry must be one word"
    assert 1 <= len(WORD) <= 24, "entry must be 1-24 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"Wrote {WORD!r} ({len(WORD)} characters) to /output/entry.txt")


if __name__ == "__main__":
    main()
