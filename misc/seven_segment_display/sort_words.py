"""Sort words in file by length into new file."""


def create_sorted_file(in_path, out_path):
    """Sort words in given file by length into new file.

    Args:
        in_path (str): file path to input file
        out_path (str): file path to output file

    """
    with open(in_path, "r") as file:
        words = file.readlines()

    with open(out_path, "w") as file:
        for word in sorted(words, key=len, reverse=True):
            file.write(word)


def main():
    """Create sorted list of english words."""
    in_path = r"C:\Users\Patrick\Documents\programming\algo\misc\seven_segment_display\words_alpha.txt"  # noqa: E501, pylint: disable=C0301
    out_path = r"C:\Users\Patrick\Documents\programming\algo\misc\seven_segment_display\words_alpha_by_len.txt"  # noqa: E501, pylint: disable=C0301

    create_sorted_file(in_path, out_path)


if __name__ == '__main__':
    main()
