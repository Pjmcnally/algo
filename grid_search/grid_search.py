#!/bin/python3

import sys, re


def build_m_string(height):
    string = ""
    for x in range(height):
        string += input()
        string += "."
        
    return string[:-1]  # slice is awkward solution to remove trailing "."


def build_q_regex(height, offset):
    string = ""
    for x in range(height):
        temp = "({input}).{l_brace}{offset}{r_brace}".format(
            input=input(), offset=offset, l_brace="{", r_brace="}")
        string += temp
        
    return string[:-len(str(offset)) - 3] # slice is awkeard solution to remove trailing offset.


def gen_answer():
    m_height, m_width = [int(x) for x in input().strip().split(" ")]
    m_string = build_m_string(m_height)
    q_height, q_width = [int(x) for x in input().strip().split(" ")]
    offset = m_width - q_width + 1
    q_string = build_q_regex(q_height, offset)

    regex = re.compile(q_string)

    if re.search(regex, m_string):
        return "YES"
    else:
        return "NO"
    

def main():
    num_tests = int(input().strip())
    for x in range(num_tests):
        print(gen_answer())



with open("grid_search_test_1.txt", "r") as f:
    print("Grid search test 1")
    def input():
        return f.readline().strip()
    main()

with open("grid_search_test_4.txt", "r") as f:
    print("Grid search test 4")
    def input():
        return f.readline().strip()
    main()

with open("grid_search_test_5.txt", "r") as f:
    print("Grid search test 5")
    def input():
        return f.readline().strip()
    main()

with open("grid_search_test_7.txt", "r") as f:
    print("Grid search test 7")
    def input():
        return f.readline().strip()
    main()
