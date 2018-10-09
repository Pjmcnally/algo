"""Fun module to play around with words and file searching."""
from collections import Counter
import os


def find_words(file, letters):
    """Find words that can be created with letters of another word.

    Any word that can be assembled from the letters of the given word counts.
    This includes a smaller word that doesn't use all of the original words
    letters.
    """
    words = []
    l_count = Counter(letters)

    with open(file, "r") as f:
        c = f.readlines()

    for line in c:
        test = True
        word = line.strip()
        w_count = Counter(word)

        for elem in w_count:
            if w_count[elem] <= l_count[elem]:
                continue
            else:
                test = False
                break

        if test:
            words.append(word)

    return words


def main():
    """Execute main function."""
    exec_dir = os.path.dirname(__file__)
    in_file = os.path.join(exec_dir, "..", "english_words", "alphabetical.txt")
    p = find_words(in_file, "vexillology")

    return len(p)


if __name__ == '__main__':
    print(main())
