def sieve_list(num):
    # Create list representing numbers between 0 and num. Assume all are prime.
    primes = [True] * (num)

    # Manually set 0 and 1 to not prime
    primes[0] = False
    primes[1] = False

    # For each n from 2 to num**.5 if n is prime set all multiples of n False.
    # For each n we only need to check from n**2 to num**.5 because n * anything
    # less than n will have already been marked as false if necessary.
    for n in range(2, int(num**.5) + 1):
        if primes[n]:
            for x in range(n**2, num, n):
                primes[x] = False

    # Convert list of true/false to list of prime integers
    return [i for i, val in enumerate(primes) if val]


def sieve_set(num):
    # Create set representing numbers between 2 and num. Assume all are prime.
    primes = {n for n in range(3, num, 2)}
    primes.add(2)

    # For each n from 2 to num**.5 if n is prime set all multiples of n False.
    # For each n we only need to check from n**2 to num**.5 because n * anything
    # less than n will have already been marked as false if necessary.
    for n in range(3, int(num**.5) + 1):
        if n in primes:
            for x in range(n**2, num, n):
                primes.discard(x)

    # Convert list of true/false to list of prime integers
    return primes


def sieve_dict(num):
    # Create dict representing numbers between 2 and num. Assume all are prime.
    primes = {n: True for n in range(3, num, 2)}
    primes[2] = True

    # For each n from 2 to num**.5 if n is prime set all multiples of n False.
    # For each n we only need to check from n**2 to num**.5 because n * anything
    # less than n will have already been marked as false if necessary.
    for n in range(2, int(num**.5) + 1):
        if primes[n]:
            for x in range(n**2, num, n):
                primes[x] = False

    # Convert list of true/false to list of prime integers
    return [i for i, val in primes.items() if val]


def main():
    print(sieve_set(1000))


if __name__ == '__main__':
    main()
