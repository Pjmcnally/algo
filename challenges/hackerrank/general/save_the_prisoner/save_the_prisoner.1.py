def main():
    cases = int(input())
    for i in range(cases):
        [inmates, sweets, prisoner] = [int(x) for x in input().strip().split(' ')]
        ##print([prisoner, (sweets) % inmates])
        last = ((prisoner + sweets - 2) % inmates) + 1
        

def input():
    return f.readline()

with open("save_the_prisoner_test_0.txt", "r") as f:
    print("\nSave the Prisoner test 1")
    main()
