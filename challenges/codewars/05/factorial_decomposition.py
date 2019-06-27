"""Solution for Codewars problem.

Kyu: 5
Name: Factorial decomposition
Link: https://www.codewars.com/kata/5a045fee46d843effa000070
"""


def decomp(n):
    """Find all prime factors of stated factorial."""
    # Calculate all needed primes once to save time
    # We only need the primes up to the square root of the original number.
    primes = primes_less_than(int(n ** 0.5))

    # Calculate all prime factors using precalculated primes
    factors = {}
    for num in range(2, n + 1):
        for prime in primes:
            while num % prime == 0:
                num //= prime
                factors[prime] = factors.get(prime, 0) + 1

        # Add remaining value if that value is not 1 (as it must be prime)
        if num != 1:
            factors[num] = factors.get(num, 0) + 1

    # Format and return output
    facts = sorted(factors.items())
    return " * ".join([f"{num}^{cnt}" if cnt > 1 else f"{num}" for num, cnt in facts])


def primes_less_than(x):
    """Sieve of Eratosthenes to calculate all prime numbers less than or equal to x."""
    # Create list to represent primality of numbers (Set 0 and 1 to False)
    primes = [True] * (x + 1)
    primes[0], primes[1] = False, False

    # For each prime number cross out all multiples of that number
    for i in range(int(x ** 0.5) + 1):
        if primes[i]:
            for num in range(i * 2, len(primes), i):
                primes[num] = False

    # Convert indexes to numbers and return as list
    return [i for i, x in enumerate(primes) if x]
