"""Solution for Codewars problem.

Kyu: 4
Name: Next bigger number with the same digits
Link: https://www.codewars.com/kata/55983863da40caa2c900004e
"""


def next_bigger(n):
    """Find next biggest number using the same digits."""
    dig_list = list(str(n))

    i = len(dig_list) - 2
    while i >= 0:
        # Look for possible swap (left digit smaller than the right digit)
        if dig_list[i] < dig_list[i + 1]:
            swap_group = dig_list[i:]
            # Find best possible swap (smallest digit bigger than current digit)
            next_big = min(x for x in swap_group if x > dig_list[i])
            swap_group.remove(next_big)
            dig_list[i:] = [next_big] + sorted(swap_group)
            return int("".join(dig_list))

        i -= 1

    return -1
