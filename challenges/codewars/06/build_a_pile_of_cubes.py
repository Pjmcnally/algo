"""Solution for Codewars problem.

Kyu: 6
Name: Build a pile of Cubes
Link: https://www.codewars.com/kata/5592e3bd57b64d00f3000047
"""

memo_dict = {1: 1}


def find_nb(m):
    # return find_nb_loop(m)
    # return find_nb_memo(m)
    return find_nb_math(m)


def find_nb_loop(m):
    """Brute force loop approach."""
    cube_count = 0
    while m > 0:
        cube_count += 1
        m -= cube_count ** 3

    return cube_count if m == 0 else -1


def find_nb_memo(m):
    """Memoized approach to find nb.

    For some reason this is slower than the looping approach.
    """
    max_value = max(memo_dict.keys())
    while max_value < m:
        cube_count = memo_dict[max_value] + 1
        max_value += (cube_count) ** 3
        memo_dict[max_value] = cube_count

    return memo_dict.get(m, -1)


def find_nb_math(m):
    """Calculate nb using mathematical formula.

    Formula for the sum of cubes = ((n * (n + 1)) / 2)**2
    We can say the following:
        m = ((n * (n + 1)) / 2)**2
        m**.5 = (n * (n + 1)) / 2
        2 * (m ** .5) = n * (n + 1)

    So we can approximate that:
        n**2 < 2 * (m ** .5) < (n + 1)**2

    And finally n < (2 * (m ** .5))**.5 < n + 1
    """
    guess = int((2 * (m ** 0.5)) ** 0.5)
    if ((guess * (guess + 1)) // 2) ** 2 == m:
        return guess
    else:
        return -1


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as test  # noqa: E402, pylint: disable=E0401

test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
