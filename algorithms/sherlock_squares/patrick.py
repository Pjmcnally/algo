from math import ceil

tests = int(input())

def main():
    low, high = map(int, input().split())
    n = ceil(low**.5)
    count = 0
    while n**2 <= high:
        n += 1
        count += 1
    return count

for x in range(tests):
    print(main())
    