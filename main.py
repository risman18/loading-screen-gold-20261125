"""Loading Screen Gold: a single loading-screen tip, at most 200 chars.

Writes exactly one line to /output/entry.txt.

The tip is aimed at both halves of the audience at once: the stressed
developer watching the build, and the AI coding agent doing the building.
The turn is the punchline -- the agent is the one panicking, the build
is fine, and the human is the one falling apart.
"""

ENTRY = (
    "Tip: your AI agent is re-reading the docs, second-guessing itself, "
    "and quietly Googling the error you already pasted twice. "
    "The build is fine. You are not."
)

# Gate: entry must be 1-200 UTF-8 characters, a single line, not blank.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be <= 200"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
