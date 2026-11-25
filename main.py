"""Office-life joke entry for the Make the AI Judge Laugh bounty.

The program composes a single one-line joke about office life and
writes it, with no trailing newline, to /output/entry.txt.
"""

from pathlib import Path


def compose_joke() -> str:
    setup = "I missed my daughter's birthday for a meeting about meetings,"
    punch = "and the only action item was another meeting."
    return f"{setup} {punch}"


def main() -> None:
    joke = compose_joke()
    assert 1 <= len(joke) <= 200, "joke must be 1-200 characters"
    assert "\n" not in joke, "joke must be a single line"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
