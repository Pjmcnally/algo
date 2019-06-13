"""Solution for Project Euler #1: Multiples of 3 and 5.

Found at: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/submissions/code/1311804538
"""  # noqa:


def sum_val(limit, div):
    """Return sum of all numbers below limit that are evenly dividable by div.

    Args:
        limit (int): The limit number (non-inclusive)
        div (int): The divisor.
    Returns:
        int: the total of all numbers below the limit evenly dividable by div

    """
    count = limit // div
    return div * count * (count + 1) // 2


def total_sum(small, big, limit):
    """Return sum of all numbers < limit that are divisible by 2 given numbers.

    Args:
        small(int): A number to use as a divisor
        big(int): A number to use as a divisor
        limit(int): The upper limit to check
    Return:
        int: Total sum of all numbers below limit divisible by small and big.

    """
    limit -= 1
    return sum_val(limit, small) + sum_val(limit, big) - sum_val(
        limit, small * big)


def main():
    """Execute main loop."""
    tests = int(input())
    small = 3
    big = 5

    for test in range(tests):
        limit = int(input())
        print(total_sum(small, big, limit))


main()
