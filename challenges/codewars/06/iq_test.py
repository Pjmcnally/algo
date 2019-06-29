"""Solution for Codewars problem.

Kyu: 6
Name: IQ Test
Link: https://www.codewars.com/kata/iq-test
"""


def iq_test(numbers):
    parity_array = [int(x) % 2 for x in numbers.split(" ")]

    if parity_array.count(0) == 1:
        return parity_array.index(0) + 1
    else:
        return parity_array.index(1) + 1


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as Test  # noqa: E402, pylint: disable=E0401

Test.assert_equals(iq_test("2 4 7 8 10"), 3)
Test.assert_equals(iq_test("1 2 2"), 1)
