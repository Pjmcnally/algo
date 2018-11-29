#!/bin/python3

import sys

def find_digits(num):
    org_num = num
    
    count = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        
        if digit != 0 and org_num % digit == 0:
            count += 1
            
    return count

def main():
    tests = int(input().strip())
    
    for x in range(tests):
        num = int(input().strip())
        print(find_digits(num))

main()
