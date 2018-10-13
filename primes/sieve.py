"""Test various implementations of Sieve of Eratosthenes.

Look into https://stackoverflow.com/questions/10249378/segmented-sieve-of-eratosthenes/10249801#10249801

"""  # noqa


def sieve_list(num):
    """Find prime numbers using Sieve and list datastructure."""
    # Create list representing numbers between 0 and num. Primality of n stored
    # at index n. Assume all numbers are prime when constructing list.
    primes = [True] * (num)

    # Manually set 0 and 1 to not prime
    primes[0] = False
    primes[1] = False

    # For each n from 2 to sqrt(num) if n is prime set all multiples of n
    # starting at n**2 to False. We only need to check from n**2 because n *
    # anything less than n will have already been marked as false previously.
    for n in range(2, int(num**.5) + 1):
        if primes[n]:
            for x in range(n**2, num, n):
                primes[x] = False

    # Convert list of true/false to list of prime integers
    return [i for i, val in enumerate(primes) if val]


def sieve_dict(num):
    """Find prime numbers using Sieve and dictionary datastructure."""
    # Create dict of numbers between 2 and num. Assume all are prime.
    primes = {n: True for n in range(2, num)}

    # For each n from 2 to sqrt(num) if n is prime set all multiples of n
    # starting at n**2 to False. We only need to check from n**2 because n *
    # anything less than n will have already been marked as false previously.
    for n in range(2, int(num**.5) + 1):
        if primes[n]:
            for x in range(n**2, num, n):
                primes[x] = False

    # Convert list of true/false to list of prime integers
    return [i for i, val in primes.items() if val]


def sieve_dict_odd(num):
    """Find prime numbers using Sieve and dict datastructure only odd nums."""
    # Create dict of odd numbers between 3 and num. Assume all are prime.
    primes = {n: True for n in range(3, num, 2)}
    primes[2] = True  # Manually add 2 to dictionary

    # For each odd n from 3 to sqrt(num) if n is prime set all multiples of n
    # starting at n**2 to False. We only need to check from n**2 because n *
    # anything less than n will have already been marked as false previously.
    for n in range(3, int(num**.5) + 1, 2):
        if primes[n]:
            for x in range(n**2, num, n):
                if x in primes:
                    primes[x] = False

    # Convert list of true/false to list of prime integers
    return sorted([i for i, val in primes.items() if val])


def sieve_set(num):
    """Find prime numbers using Sieve and set datastructure."""
    # Create set of numbers between 2 and num. Assume all are prime.
    primes = {n for n in range(2, num)}

    # For each odd n from 2 to sqrt(num) if n is prime remove all multiples of
    # n starting at n**2. We only need to check from n**2 because n *
    # anything less than n will have already been marked as false previously.
    for n in range(2, int(num**.5) + 1):
        if n in primes:
            for x in range(n**2, num, n):
                primes.discard(x)

    # Convert list of true/false to list of prime integers
    return sorted(primes)


def sieve_set_odd(num):
    """Find prime numbers using Sieve and set datastructure only odd nums."""
    # Create set of numbers between 2 and num. Assume all are prime.
    primes = {n for n in range(3, num, 2)}
    primes.add(2)

    # For each odd n from 3 to sqrt(num) if n is prime remove all multiples of
    # n starting at n**2. We only need to check from n**2 because n *
    # anything less than n will have already been marked as false previously.
    for n in range(3, int(num**.5) + 1, 2):
        if n in primes:
            for x in range(n**2, num, n):
                primes.discard(x)

    # Convert list of true/false to list of prime integers
    return sorted(primes)


def main():
    """Execute main function."""
    print(sieve_list(200))


if __name__ == '__main__':
    main()
