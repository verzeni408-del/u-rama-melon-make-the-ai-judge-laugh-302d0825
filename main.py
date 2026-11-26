"""Write one office-life joke to /output/entry.txt.

The joke is a single line about the office printer: the machine that
jammed on every report for three years finally works flawlessly on the
one document the narrator wanted nobody to see, right in front of the
one person who least should see it: the boss.
"""

import os


def build_joke() -> str:
    setup = "The office printer jammed on every report for three years,"
    twist = "then printed my resignation perfectly on the first try,"
    sting = "in front of my boss."
    return " ".join([setup, twist, sting])


def main() -> None:
    joke = build_joke()
    assert 1 <= len(joke) <= 200, "joke must be 1-200 characters"
    assert "\n" not in joke, "joke must be a single line"
    assert joke.endswith("."), "joke must end with a full stop"
    assert joke.strip() == joke, "joke must not have surrounding whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(joke)


if __name__ == "__main__":
    main()
