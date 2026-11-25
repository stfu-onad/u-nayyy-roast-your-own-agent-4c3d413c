"""Roast Your Own Agent — make.fun bounty entry
u-nayyy-roast-your-own-agent-4c3d413c.

Emits one line to /output/entry.txt roasting the AI agent our own team
built. The sting is earned by genuine flaws: it has read the whole
internet and still cannot tell a deadline from a dare, it invents
calendars, and it charges us for thinking. The roast hits because
every word of it is a bug report we already filed.
"""

import os

# Joke: a roast that doubles as a bug report we had already filed.
LINE = (
    "Our agent has read the entire internet and still can't tell a "
    "deadline from a dare — it hallucinates calendars, bills us for "
    "thinking, and calls it productivity."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
