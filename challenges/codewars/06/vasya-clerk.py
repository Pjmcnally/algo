"""Solution for Codewars problem.

Kyu: 6
Name: Clerk
Link: https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
"""

from collections import defaultdict


def tickets(people):
    till = defaultdict(lambda: 0)

    for i in people:
        if not get_change(25, i, till):
            return "NO"

    return "YES"


def get_change(cost, payment, till):
    if payment < cost:
        return False

    change_required = payment - cost
    while change_required:
        possible_change = list(
            x for x in till.keys() if x <= change_required and till[x] > 0
        )
        if not possible_change:
            return False

        temp_change = max(possible_change)
        till[temp_change] -= 1
        change_required -= temp_change

    till[payment] += 1
    return True


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as test  # noqa: E402, pylint: disable=E0401

test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
