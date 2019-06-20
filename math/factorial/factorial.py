from datetime import datetime, timedelta
from math import factorial


def func_test(n, func_list):
    """ 3 methods of calculating factorial"""

    results = []
    for func in func_list:
        start_time = datetime.now()
        results.append(func(n))
        end_time = datetime.now()
        total_seconds = timedelta.total_seconds(end_time - start_time)

        print(f"\n{func.__name__} took {total_seconds} seconds.")

    if len(set(results)) == 1:
        print("All output answers are the same!")


def factorial_while(n):
    """Calculate the factorial of "n" using a while loop."""
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total


def factorial_for(n):
    """Calculate the factorial of "n" using a for loop."""
    total = 1
    for elem in range(1, n + 1):
        total *= elem
    return total


def factorial_python(n):
    """Calculate the factorial of "n" using the python factorial function."""
    total = factorial(n)
    return total


def main():
    functions = [factorial_while, factorial_for, factorial_python]
    func_test(100000, functions)


main()
