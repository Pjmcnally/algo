def brute(n, k, c):
    i = 0 
    e = 100
    while (i + k) % n != 0:
        i += k
        e -= 1 + (2 * c[i])
    e -= 1 + (2 * c[0])
    return e
            
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

print(brute(n, k, c))
