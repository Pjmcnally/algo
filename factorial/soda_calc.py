import datetime
from math import factorial


def test_fact(n):
    """runs 3 methods of calculating factorial"""

    def factorial_calc(n):
        """calculates the factorial of "n" using a while loop.  Also tracks how long it takes"""
        start = datetime.datetime.now()
        calc_total = 1
        while n > 0:
            calc_total *= n
            n -= 1
        end = datetime.datetime.now()
        calc_delta = end - start
        print("\nFactorial calc process (while loop) took {} seconds.\n".format(datetime.timedelta.total_seconds(calc_delta)))
        

    def factorial_rev(n):
        """calculates the factorial of "n" using a for loop.  Also tracks how long it takes"""
        start = datetime.datetime.now()
        rev_total = 1
        for elem in range(1, n+1):
            rev_total *= elem
        end = datetime.datetime.now()
        rev_delta = end - start
        print("\nFactorial rev process (for loop) took {} seconds.\n".format(datetime.timedelta.total_seconds(rev_delta)))

    def factorial_test(n):
        """calculates the factorial of "n" using the python factorial function.  Also tracks how long it takes"""
        start = datetime.datetime.now()
        test_total = factorial(n)
        end = datetime.datetime.now()
        test_delta = end - start
        print("\nFactorial process (built in function) took {} seconds.\n".format(datetime.timedelta.total_seconds(test_delta)))


    a = factorial_calc(n)
    b = factorial_rev(n)
    c = factorial_test(n)
    if a == b == c:
        print("All output answers are the same!")

test_fact(500000)



