"""Python module to count a letter characters in a file."""
from collections import Counter
import os


def count_alpha(file_path):
    """Count letter characters in specified file."""
    # Read file, get content, build counter
    with open(file_path, "r") as f:
        content = f.read().lower()
    letters = Counter(content)

    # Remove from counter any items that are not alphabetical
    for item in list(letters.keys()):
        if not item.isalpha():
            del letters[item]

    return letters


def format_output(letters):
    """Display formated output."""
    for let, count in sorted(letters.items()):
        print(f"{let}: {count}")
    print(f"Total Letters: {sum(letters.values())}")


def main(display_full=False):
    """Execute main function."""
    _dir = os.path.dirname(__file__)
    file_path = os.path.join(_dir, "..", "english_words", "alphabetical.txt")

    letters = count_alpha(file_path)

    if display_full:  # Print results and total
        format_output(letters)
    else:
        return sum(letters.values())


if __name__ == '__main__':
    print(main())
