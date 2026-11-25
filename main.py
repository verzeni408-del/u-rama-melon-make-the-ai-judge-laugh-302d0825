"""Write one office-life joke to /output/entry.txt.

The joke is a single line about office life. The program writes it
exactly, with no trailing newline, so the file holds only the joke.

Why this line: the setup is a true office observation (HR closes
complaints like support tickets), the person in it is the one harmed,
and the last words carry the dark turn (the spreadsheet, not the
human, decides he is fine). One sentence, 103 characters.
"""

import os

JOKE = "HR closed my burnout complaint as resolved. I still can't sleep, but the spreadsheet says I'm fine now."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
