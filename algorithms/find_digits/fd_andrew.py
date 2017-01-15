"""def main(n):
    count = 0
    digits = [int(x) for x in n]
    n = int(n)
    for digit in digits:
        if digit != 0:
            if n % digit == 0: 
                count += 1
    return count
    
    

t = int(input().strip())
for a0 in range(t):
    n = input().strip()
    print(main(n))"""

def main(n):
    count = 0
    n_mod = n
    while n_mod // 10 != 0:
        digit = n_mod % 10
        n_mod = n_mod // 10
        print(digit)
        if digit != 0:   
            if n % digit == 0:
                count += 1
    return count
    
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    main(n)