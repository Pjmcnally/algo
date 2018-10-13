"""Find all prime factors of a given number."""
from math import factorial

# def prime_factors_brute_all(num):
#     """Return all prime factors of num. Unoptimized checking all numbers."""
#     factors = []

#     # Check all numbers from 2 through n
#     for n in range(2, num):
#         while num % n == 0:
#             factors.append(n)
#             num //= n

#     # If any piece of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors

# def prime_factors_brute_odd(num):
#     """Return all prime factors of num. Unoptimized checking only odd."""
#     factors = []

#     # Extract all factors where factor = 2
#     while num % 2 == 0:
#         factors.append(2)
#         num //= 2

#     # Check all odd numbers from 3 to num.
#     for n in range(3, num, 2):
#         while num % n == 0:
#             factors.append(n)
#             num //= n

#     # If any piece of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors

# def prime_factors_opt_all(num):
#     """Return all prime factors of num. Optimized method checking all nums."""
#     factors = []

#     # Check all n from 2 to sqrt(num)
#     for n in range(2, int(num**.5) + 1):
#         while num % n == 0:
#             factors.append(n)
#             num //= n

#     # If any piece of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors


def prime_factors_opt_odd(num):
    """Return all prime factors of num. Optimized method checking odd nums."""
    factors = []

    # Extract all factors where factor = 2
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    # Check all odd numbers from 3 to sqrt(num).
    for n in range(3, int(num**.5) + 1, 2):
        while num % n == 0:
            factors.append(n)
            num //= n

        # If any piece of num remains add to factor list.
    if num > 1:
        factors.append(num)

    return factors


# def prime_factors_while_all(num):
#     """Return all prime factors of num. Optimized method checking odd nums."""
#     factors = []
#     n = 2

#     # Check all odd numbers from 3 to sqrt(num).
#     while num > n:
#         while num % n == 0:
#             factors.append(n)
#             num //= n
#         n += 1

#         # If any piece of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors

# def prime_factors_while_all_opt(num):
#     """Return all prime factors of num. Optimized method checking odd nums."""
#     factors = []
#     max_check = int(num**.5)
#     n = 2

#     # Check all odd numbers from 3 to sqrt(num).
#     while num > n and n <= max_check:
#         while num % n == 0:
#             factors.append(n)
#             num //= n
#         n += 1

#         # If any piece of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors


def prime_factors_while_odd_opt(num):
    """Return all prime factors of num. Optimized method checking odd nums."""
    factors = []
    max_check = int(num**.5)  # Set highest number to check (stop at sqrt(num))
    n = 3

    # Extract all factors where factor = 2
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    # Check all odd numbers from 3 to sqrt(num).
    while num > n and n <= max_check:
        while num % n == 0:
            factors.append(n)
            num //= n
        n += 2

    # If any part of num remains add to factor list.
    if num > 1:
        factors.append(num)

    return factors


def get_functions():
    """Return all functions in this module (except for default)."""
    import sys
    import inspect
    import json

    default = {'main', 'get_functions'}
    raw_functions = inspect.getmembers(sys.modules[__name__],
                                       inspect.isfunction)
    return [x[0] for x in raw_functions if x[0] not in default]


def main():
    """Execute main function."""
    print(prime_factors_while_odd_opt(factorial(7)))


if __name__ == '__main__':
    main()
