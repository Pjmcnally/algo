"""Find the longest english word representable on a seven segment display.

This is based on the YouTube video by Tom Scott found here:
https://www.youtube.com/watch?v=zp4BMR88260&feature=youtu.be
"""

import os
import re


def find_longest_words(file_path):
    """Find longest word representable on a seven segment display."""
    # Get list of words to check sort longest first.
    with open(file_path, "r") as file:
        sorted_words = sorted(file.read().splitlines(), reverse=True, key=len)

    # Build regex of letters unrepresentable on a seven segment display
    pattern = re.compile(r'^[^gkmqvwxzio]+$')  # cspell: ignore gkmqvwxzio

    out_list = []
    max_words = 10

    for word in sorted_words:
        if pattern.search(word):
            out_list.append(word)

        # If you have found the desired number of words stop
        if len(out_list) == max_words:
            break

    return out_list


def main():
    """Execute main function."""
    _dir = os.path.dirname(__file__)
    file_path = os.path.join(_dir, "..", "english_words", "alphabetical.txt")

    for word in find_longest_words(file_path):
        print(word)


if __name__ == '__main__':
    main()
