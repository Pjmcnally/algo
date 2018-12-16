from math import log10 

test_case = "1 2000000 45684660"

start, end, div = [int(x) for x in test_case.strip().split(" ")]

def patrick(start, end, div):
    total = 0
    for day in range(start, end + 1):
        if abs(day - int(str(day)[::-1])) % div == 0:
            total += 1
            
    return total


def andrew(i, j, k):
    count = 0
    for val in range(i, j + 1):
        last = val % 10
        first = val // (10 ** len(str(val)))
        if (abs(last - first)* 9) % k == 0:
            count += 1
            print(val)
            
    return count


print(patrick(start, end, div))
print(andrew(start, end, div))