from pathlib import Path

FRAGMENTS = [
    "Our agent has read the entire internet and still can't tell a ",
    "deadline from a dare — it hallucinates calendars, bills us for ",
    "thinking, and calls it productivity.",
]

ENTRY_PATH = Path("/output/entry.txt")
LIMIT = 200


def build_line(segments):
    line = ""
    for segment in segments:
        line += segment
    return line.strip()


def check_line(line):
    problems = []
    if not line.strip():
        problems.append("entry must not be only whitespace")
    if not 1 <= len(line) <= LIMIT:
        problems.append(f"line is {len(line)} chars")
    if "\n" in line:
        problems.append("entry must be a single line")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry must be UTF-8 text")
    if problems:
        raise ValueError("; ".join(problems))


def write_entry(line, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")
    return len(line)


def main():
    line = build_line(FRAGMENTS)
    check_line(line)
    count = write_entry(line, ENTRY_PATH)
    print(f"wrote {count} chars to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
