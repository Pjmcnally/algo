"""Find all prime factors of a given number."""

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
#     """Return all prime factors of num. Optimized method checking all n."""
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

# def prime_factors_opt_odd(num):
#     """Return all prime factors of num. Optimized method checking odd n."""
#     factors = []

#     # Extract all factors where factor = 2
#     while num % 2 == 0:
#         factors.append(2)
#         num //= 2

#     # Check all odd numbers from 3 to sqrt(num).
#     for n in range(3, int(num**.5) + 1, 2):
#         while num % n == 0:
#             factors.append(n)
#             num //= n

#         # If any piece of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors

# def prime_factors_while_all(num):
#     """Return all prime factors of num. Optimized method checking odd n."""
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
#     """Return all prime factors of num. Optimized method checking odd n."""
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


def prime_factors(num):
    """Return all prime factors of num. Optimized method checking odd nums."""
    factors = []
    n = 3

    # Extract all factors where factor = 2
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    # Check all odd numbers from 3 to sqrt(num).
    while n**2 <= num:
        while num % n == 0:
            factors.append(n)
            num //= n
        n += 2

    # If any part of num remains add to factor list.
    if num > 1:
        factors.append(num)

    return factors


# def prime_factors_alt(num):
#     """Return all prime factors of num. Optimized method checking odd n."""
#     factors = []
#     n = 3

#     # Extract all factors where factor = 2
#     while num % 2 == 0:
#         factors.append(2)
#         num //= 2

#     # Check all odd numbers from 3 to sqrt(num).
#     while n**2 <= num:
#         if num % n:
#             n += 2
#         else:
#             factors.append(n)
#             num //= n

#     # If any part of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors

# def prime_factors_pre_primes(num, primes):
#     """Return all prime factors of num. Use pre-built list of primes.

#     Surprisingly this is not significantly faster even if the list of primes
#     is pre-calculated and not time. If it is included in the timing this
#     method is much slower.
#     """
#     factors = []

#     for n in primes:
#         if n**2 > num:
#             break

#         while num % n == 0:
#             factors.append(n)
#             num //= n

#     # If any part of num remains add to factor list.
#     if num > 1:
#         factors.append(num)

#     return factors


def get_functions():
    """Return all functions in this module (except for default)."""
    import sys
    import inspect

    default = {'main', 'get_functions'}
    raw_functions = inspect.getmembers(sys.modules[__name__],
                                       inspect.isfunction)
    return [x[0] for x in raw_functions if x[0] not in default]


def main():
    """Execute main function."""
    print(prime_factors(5 * 6 * 7 * 8))


if __name__ == '__main__':
    main()
