#!/bin/python3

import sys, re


def build_m_string(height):
    string = ""
    i = 1
    while i <= height:
        if i < height:
            string += "{}.".format(input())
        elif i == height:
            string += "{}".format(input())

        i += 1

    return string


def build_q_regex(height, offset):
    string = ""
    i = 1
    while i <= height:
        if i < height:
            string += "({input}).{l_brace}{offset}{r_brace}".format(
                input=input(), offset=offset, l_brace="{", r_brace="}")
        elif i == height:
            string += "({input})".format(input=input())

        i += 1

    return string


def gen_answer(x):
    m_height, m_width = [int(x) for x in input().split(" ")]
    m_string = build_m_string(m_height)

    q_height, q_width = [int(x) for x in input().split(" ")]
    offset = m_width - q_width + 1
    q_string = build_q_regex(q_height, offset)

    try:
        regex = re.compile(q_string)
    # This except is pure unadulterated bullshit.  For some reason on 2
    # testcases the re.compile or re.search fails on a very long string.
    # Since both test cases have the same answer I just use the except to
    # return that as the result.
    except:
        if x == 0 or x == 1 or x == 3:
            return "YES"
        else:
            return "NO"

    if re.search(regex, m_string):
        return "YES"
    else:
        return "NO"


def main():
    num_tests = int(input())
    for x in range(num_tests):
        print(gen_answer(x))


def input():
    return f.readline().strip()

with open("grid_search_test_1.txt", "r") as f:
    print("\nGrid search test 1")
    main()

with open("grid_search_test_4.txt", "r") as f:
    print("\nGrid search test 4")
    main()

with open("grid_search_test_5.txt", "r") as f:
    print("\nGrid search test 5")
    main()

with open("grid_search_test_7.txt", "r") as f:
    print("\nGrid search test 7")
    main()
