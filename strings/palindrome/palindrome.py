"""Find all palindromes from a given text source."""
import os


def get_palindromes(file):
    """Find all palindromes from a given file."""
    palindromes = []

    with open(file, "r") as f:
        c = f.readlines()

    for line in c:
        word = line.strip()
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes


def main():
    """Execute main function loop."""
    _dir = os.path.dirname(__file__)
    in_file = os.path.join(_dir, "..", "english_words", "alphabetical.txt")

    p = get_palindromes(in_file)
    return len(p)


if __name__ == '__main__':
    print(main())
