from collections import Counter
import os


def main():
    """Count Characters in specified file."""
    _dir = os.path.dirname(__file__)
    file_path = os.path.join(_dir, "..", "english_words", "alphabetical.txt")

    with open(file_path, "r") as f:
        content = f.read().lower()

    a = Counter(content)
    for let, count in sorted(a.items()):
        print(repr(let), count)


if __name__ == '__main__':
    main()
