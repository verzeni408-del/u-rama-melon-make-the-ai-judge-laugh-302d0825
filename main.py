"""Office-life joke entry for the Make the AI Judge Laugh bounty.

The program composes a single one-line joke about office life and
writes it, with no trailing newline, to /output/entry.txt.
"""

from pathlib import Path

# The joke text lives in module constants so compose() stays trivial
# and any future edit touches exactly one place.
JOKE_SETUP = "I missed my daughter's birthday for a meeting about meetings,"
JOKE_PUNCH = "and the only action item was another meeting."


def compose_joke() -> str:
    return f"{JOKE_SETUP} {JOKE_PUNCH}"


def main() -> None:
    joke = compose_joke()
    assert 1 <= len(joke) <= 200, "joke must be 1-200 characters"
    assert "\n" not in joke, "joke must be a single line"
    assert "  " not in joke, "joke must not contain double spaces"
    assert joke.endswith("."), "joke must end with a period"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
