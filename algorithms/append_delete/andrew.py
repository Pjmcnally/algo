def main(s, t, k):
    lens = len(s)
    lent = len(t)
    if k >= lens + lent:
        return 'Yes'
    else:       
        i = 0
        while i < min(lens, lent) and s[i] == t[i]:
            i += 1
    op_min = lens + lent - 2 * i
    if k >= op_min and (k - op_min) % 2 == 0:
        return 'Yes'
    else:
        return 'No'
    
s = input().strip()
t = input().strip()
k = int(input().strip())

print(main(s, t, k))
