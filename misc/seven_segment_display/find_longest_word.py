"""Find the longest english word representable on a seven segment display.

This is based on the YouTube video by Tom Scott found here:
https://www.youtube.com/watch?v=zp4BMR88260&feature=youtu.be
"""

import re


def main():
    """Find longest word representable on a seven segment display."""
    path = r"C:\Users\Patrick\Documents\programming\algo\misc\seven_segment_display\words_alpha_by_len.txt"  # noqa: E501, pylint: disable=C0301

    # Get sorted list of words to check
    with open(path, "r") as file:
        sorted_words = file.read().splitlines()

    # Build regex of unrepresentable letters
    bad_lets = re.compile(r'^[^gkmqvwxzio]+$')  # cspell: ignore gkmqvwxzio

    out_list = []
    max_words = 10

    for word in sorted_words:
        if bad_lets.search(word):
            out_list.append(word)

        if len(out_list) == max_words:
            break

    for word in out_list:
        print(word)


if __name__ == '__main__':
    main()
