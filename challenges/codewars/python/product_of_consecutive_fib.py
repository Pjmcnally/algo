"""Code for Product of consecutive Fib numbers on Codewars.com.

https://www.codewars.com/kata/product-of-consecutive-fib-numbers/python
"""

import test

FIB = {"max": 1, 0: 0, 1: 1}


def productFib(prod):
    """Calculate product fib using external fib func."""
    i = 0
    while fib(i) * fib(i + 1) <= prod:
        if fib(i) * fib(i + 1) == prod:
            return [fib(i), fib(i + 1), True]
        i += 1

    return [fib(i), fib(i + 1), False]


def productFib_no_mem(prod):
    """Calculate product fib.

    This function is self contained but uses no memoization so is slower.
    """
    a, b = 0, 1
    while a * b < prod:
        b, a = a + b, b

    return [a, b, a * b == prod]


def fib(n):
    """Memoized func to calculate fibonacci of n (non recursive)."""
    for i in range(FIB["max"] + 1, n + 1):
        FIB[i] = FIB[i - 1] + FIB[i - 2]
        FIB["max"] = i

    return FIB[n]


def fib_recursive(n):
    """Memoized func to calculate fibonacci of n (recursive)."""
    if n not in FIB:
        FIB[n] = fib(n - 1) + fib(n - 2)

    return FIB[n]


test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])
