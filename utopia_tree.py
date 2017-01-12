import sys
from timeit import timeit

array = [10000]


def linear_while(n):
    height = 1
    for x in range(1, n+1):
        if x % 2 == 0:
            height += 1
        else:
            height *= 2
    return height


def recursive(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return recursive(n-1) + 1
    else:
        return recursive(n-1) * 2


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


def test_num(num):
    if linear_while(num) == recursive(num) == line_2_o1(num) == line_1_o1(num) == line_1_o1_mod(num):
        print("Yay!")
    else:
        print("Booo!")

test_num(950)

# def test(name):
#     val = timeit(
#             "{}".format(name + "(array)"),
#             setup="from __main__ import {}, array".format(name),
#             number=1)
#     return name, val


# def array_test(function, array):
#     results = []
#     for val in array:
#         results.append(function(val))

#     return results


# def main():
#     org_rec_limit = sys.getrecursionlimit()
#     print(org_rec_limit)
#     sys.setrecursionlimit(15000)
#     new_rec_limit = sys.getrecursionlimit()
#     print(new_rec_limit)

#     func_list = ["linear_while", "recursive", "line_2_o1", "line_1_o1",
#                  "line_1_o1_mod"]
#     for x in func_list:
#         name, val = test(x)
#         print("{:<15} took   {:<20}".format(name, val))


# main()
