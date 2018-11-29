from math import ceil, floor

def main():
    tests = int(input())
    for x in range(tests):
        low, high = (int(x) for x in input().strip().split(' '))
        print(sqr_between(low, high))
        print(quick_sqr_between(low, high))


def sqr_between(low, high):
    n = ceil(low**.5)
    count = 0
    while n**2 <= high:
        n += 1
        count += 1
    return count


def quick_sqr_between(low, high):
    results = int(floor(high**.5) - ceil(low**.5)) + 1
    return results
    
    
main()