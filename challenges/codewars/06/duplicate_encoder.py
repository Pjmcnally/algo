"""Solution for Codewars problem.

Kyu: 6
Name: Duplicate Encoder
Link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
"""

from collections import Counter


def duplicate_encode(word):
    """Encode word by whether character is duplicated."""
    c = Counter(word.lower())
    return "".join("(" if c[x] == 1 else ")" for x in word.lower())


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as Test  # noqa: E402, pylint: disable=E0401

# Test.assert_equals(duplicate_encode("din"), "(((")
# Test.assert_equals(duplicate_encode("recede"), "()()()")
Test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
Test.assert_equals(duplicate_encode("(( @"), "))((")
