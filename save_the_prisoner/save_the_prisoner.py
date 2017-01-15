def main():
    tests = int(input().strip())
    for x in range(tests):
        print(find_prisoner())


def find_prisoner():
    prisoners, sweets, p_id = (int(x) for x in input().strip().split(' '))

    poisoned = (p_id + sweets - 1 - 1) % (prisoners) + 1

    return poisoned


def input():
    return f.readline().strip()

with open("save_the_prisoner_test_0.txt", "r") as f:
    print("\nSave the Prisoner test 1")
    main()
