import sys
from timeit import timeit

array = range(10000)

# ==============================
# untested functions


# Slower than while and overflows if number gets big
def recursive(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return recursive(n-1) + 1
    else:
        return recursive(n-1) * 2

# =============================
# functions to be tested


def linear_while(n):
    height = 1
    for x in range(1, n+1):
        if x % 2 == 0:
            height += 1
        else:
            height *= 2
    return height


def line_2_o1(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return (2 ** ((n // 2) + 1)) - 1
    else:
        return (2 ** ((n + 1) // 2 + 1)) - 2


def line_1_o1(n):
    mod = n % 2
    return (2 ** ((n + mod) // 2 + 1)) - 1 - (mod)


def line_1_o1_mod(n):
    if n:
        mod = n % 2
        return (2 ** ((n + mod) // 2 + 1)) - 1 - (mod)
    else:
        return 1


def growth_dict(num):
    res_dict = {}
    for val in range(num + 1):
        total = res_dict.get(val - 1, 0)
        if val % 2 == 0:
            res_dict[val] = total + 1
        else:
            res_dict[val] = total * 2
    return res_dict


def pre_test(funcs, nums):
    results = []

    for func in funcs:
        results.append(test_wrap(func, nums))

    if all(x == results[0] for x in results):
        print("All fuctions generating same answer")
    else:
        print("Some function(s) not generating same answer")


def test_wrap(function, array):
    results = []

    if function == growth_dict:
        num = max(array)
        res = growth_dict(num)
        for x in array:
            results.append(res[x])
        return results
    else:
        for val in array:
            results.append(function(val))

        return results


def test(func):
    val = timeit(
        "test_wrap({}, array)".format(func.__name__),
        setup="from __main__ import test_wrap, array, {}".format(func.__name__),  # noqa
        number=3
    )
    return val


def main():
    func_list = [
        linear_while,
        growth_dict,
        line_2_o1,
        line_1_o1,
        line_1_o1_mod
    ]

    test_array = [0, 1, 10, 100, 1000]
    pre_test(func_list, test_array)

    for x in func_list:
        val = test(x)
        print("{:<15} took   {:e}".format(x.__name__, val))


main()
