"""Answer to https://www.codewars.com/kata/59901cd68fc658ab6c000025/."""


def distribute(m, n):
    """Solve distribute with list multiplication.

    Big O(n). Not sure why but this solution is significantly faster than
    using a list comprehension.
    """
    if n <= 0:
        return []
    elif m <= 0:
        return [0] * n
    else:
        x_candy = m % n  # Number of people that get extra candy
        b_candy = m // n  # The base number of candy that people get.
        return ([b_candy] * (n - x_candy)) + ([b_candy + 1] * x_candy)


# def distribute(m, n):
#     """Solve distribute with list comprehension.

#     Big O(n). Not sure why but this solution is significantly slower than
#     multiplying lists.
#     """
#     if n <= 0:
#         return []

#     # Calculate base number of candy and extra candy left over.
#     b_candy, x_candy = divmod(max(m, 0), n)

#     # (i < x_candy) = 1 or 0 (true or false) and adds "extra" candy.
#     return [b_candy + (i < x_candy) for i in range(n)]

# def distribute(m, n):
#     """Solve Distribute.

#   Iterative solution. Big O(m).
#   """
#     if n <= 0:
#         return []

#     out = [0] * n
#     for i in range(m):
#         out[i % n] += 1

#     return out

# Timing information:
# ==============================================================================
# Timing list multiplication function
# python -m timeit -s "a = 10; b = 100; n = 1000000" "([a] * (n - b)) + ([a + 1] * b)"  # noqa
# 50 loops, best of 5: 7.57 msec per loop

# Timing List Comprehension function:
# python -m timeit -s "b = 10; x = 100; n = 1000000" "[b + (i < x) for i in range(n)]"  # noqa
# 1 loop, best of 5: 83.9 msec per loop

# Tests below this line
# ==============================================================================
import codewarstest as Test  # noqa: E402, pylint: disable=C0413

Test.assert_equals(sorted(distribute(-5, 10)), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
Test.assert_equals(sorted(distribute(0, 10)), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Test.assert_equals(sorted(distribute(5, 10)), [0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
Test.assert_equals(sorted(distribute(10, 10)), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
Test.assert_equals(sorted(distribute(10000000, 2)), [5000000, 5000000])
Test.assert_equals(sorted(distribute(0, 10000)), [0] * 10000, "m=0, n=10000")
Test.assert_equals(distribute(-5, 0), [])
Test.assert_equals(distribute(0, 0), [])
Test.assert_equals(distribute(5, 0), [])
Test.assert_equals(distribute(10, 0), [])
Test.assert_equals(distribute(15, 0), [])
Test.assert_equals(distribute(-5, -5), [])
Test.assert_equals(distribute(0, -5), [])
Test.assert_equals(distribute(5, -5), [])
Test.assert_equals(distribute(10, -5), [])
Test.assert_equals(distribute(15, -5), [])
