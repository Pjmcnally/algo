from bisect import bisect
import numpy as np
import timeit


def prime_product(n):
    bisect_point = bisect(primes, n // 2)

    # If n is odd then pair must be (2, n - 2) or nothing. This is because 2 is the
    # only even prime and to get an odd number you must add even + odd.
    if n % 2:
        return 2 * (n - 2) if n - 2 in prime_set else 0

    # Check half of prime list (starting from the middle). Return product of first pair found
    for prime in primes[:bisect_point][::-1]:
        if n - prime in prime_set:
            return prime * (n - prime)

    return 0  # Return 0 if no valid pair found.


def get_primes_simple(n):
    """Sieve of Eratosthenes to calculate all primes less than or equal to n.

    Return set of primes.
    """
    primes = [True] * (n + 1)

    for num in range(2, int(n ** 0.5) + 1):
        if primes[num]:
            primes[num * 2 :: num] = [False] * len(primes[num * 2 :: num])

    return [i for i, x in enumerate(primes) if x and i > 1]


def get_primes_odd(n):
    """Sieve of Eratosthenes to calculate all primes less than or equal to n.

    Return set of primes.
    """
    primes = [True] * (n + 1)

    # Only examine odd numbers (We will add 2 to the final results)
    for num in range(3, int(n ** 0.5) + 1, 2):
        if primes[num]:
            # num * anything less than itself is already crossed out.
            # We can use num * 2 as a step because num + num will be even. Using num * 2 hits only odd numbers.
            primes[num ** 2 :: num * 2] = [False] * len(primes[num ** 2 :: num * 2])

    return [2] + [i for i in range(3, n + 1, 2) if primes[i]]


def get_primes_np(n):
    """Sieve of Eratosthenes to calculate all primes less than or equal to n.

    Return set of primes.
    """
    sieve = np.ones(n + 1, dtype=np.bool)

    for num in range(3, int(n ** 0.5), 2):
        if sieve[num]:
            sieve[num ** 2 :: num * 2] = False

    return [2] + [i for i in range(3, n + 1, 2) if sieve[i]]


if __name__ == "__main__":
    # Calculate all primes up to max but only calculate primes once. Then reference master prime list in all test cases.
    max_input = 100000
    primes = get_primes_np(max_input)
    prime_set = set(primes)


"""
Thanks for the feedback. I spent some time thinking about ways to optimize this further.

I tried a slight optimization of returning the primes as a dictionary (instead of a set). Using Python 3.6 it is (generally) safe to assume that they items in the dictionary will be saved in the same order as they were entered. Then I was able to only iterate over half of the keys which saved some time.

Thinking about it more it seems that the answer will always be the set nearest to the center of the list of primes. I created another solution using Bisect is another improvement on speed. Extending this I then used memoization to calculate the primes only once and to reference that list in the other functions. This is my currently fastest solution.

If you have any other specific suggestions as to how I could optimize this I would be happy to hear them.

The chart below reflects test runs done using the full test set. I realize this can fluctuate due to the random test but for this purpose seemed sufficient.

||Orig Solution|Dict Solution|Bisect Solution|Memoized-Bisect Solution|
|---|----|----|----|----|
|Avg|4238|3922|3777|2437|
|Run|3632|3370|3150|2105|
|Run|3691|3582|3453|2298|
|Run|3861|3665|3542|2361|
|Run|3877|3817|3581|2378|
|Run|4190|3953|3633|2406|
|Run|4438|4034|3726|2425|
|Run|4574|4041|3889|2541|
|Run|4596|4167|4188|2602|
|Run|4727|4229|4277|2616|
|Run|4791|4363|4334|2637|
"""
