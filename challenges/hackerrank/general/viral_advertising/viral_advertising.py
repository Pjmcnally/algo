# Patrick's
# =======================

days = int(input().strip())

def recursive(num):
    if num == 1:
        return 2, 2
    else:
        val, tot = recursive(num - 1)
        new_val = (3 * val)//2
        return new_val, new_val + tot

val, tot = recursive(days)
print(tot)


# Andrew's stuff
# ===========
n = int(input()) - 1
people = 2
new_people = 2
for i in range(n):
    new_people = (new_people * 3) // 2
    people += new_people
print(people)