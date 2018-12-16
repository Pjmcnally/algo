from math import ceil

def main(a, b):
    num1 = ceil(a**0.5)
    num = num1
    while  num**2 <= b: 
        num += 1
    return num - num1

t = int(input().strip())
for i in range(t):
    a, b = (int(x) for x in input().strip().split(' '))
    print(main(a,b))