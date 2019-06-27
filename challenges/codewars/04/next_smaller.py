"""Solution for Codewars problem.

Kyu: 4
Name: Next smaller number with the same digits
Link: https://www.codewars.com/kata/5659c6d896bc135c4c00021e
"""


def next_smaller(n):
    """Find next smallest number using the same digits."""
    dig_list = list(str(n))

    i = len(dig_list) - 2
    while i >= 0:
        # Look for possible swap (left digit is bigger than the right digit)
        if dig_list[i] > dig_list[i + 1]:
            swap_group = dig_list[i:]
            # Find best possible swap (biggest digit smaller than current digit)
            next_small = max(x for x in swap_group if x < dig_list[i])
            # Check for invalid swap of 0 to front of number
            if i == 0 and next_small == "0":
                return -1
            swap_group.remove(next_small)
            dig_list[i:] = [next_small] + sorted(swap_group, reverse=True)
            return int("".join(dig_list))

        i -= 1

    return -1
