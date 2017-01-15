def main():
    tests = int(input().strip())
    for x in range(tests):
        print(find_prisoner())


def find_prisoner():
    prisoners, sweets, p_id = (int(x) for x in input().strip().split(' '))

    final_id = (p_id + sweets - 1) % (prisoners)

    if final_id:
        return final_id
    else:
        return prisoners


def input():
    return f.readline().strip()

with open("save_the_prisoner_test_0.txt", "r") as f:
    print("\nSave the Prisoner test 1")
    main()
