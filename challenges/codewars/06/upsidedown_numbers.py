def solve(a, b):
    res = []
    nums = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    for num in range(a, b):
        num = str(num)
        i, j = 0, len(num) - 1
        valid = True

        while i <= j:
            if num[i] != nums.get(num[j]):
                valid = False
                break
            i += 1
            j -= 1

        if valid:
            res.append(num)

    return len(res)


solve(0, 10000)

# import codewarstest as Test
# Test.assert_equals(solve(0, 10), 3)
# Test.assert_equals(solve(10, 100), 4)
# Test.assert_equals(solve(100, 1000), 12)
# Test.assert_equals(solve(1000, 10000), 20)
# Test.assert_equals(solve(10000, 15000), 6)
# Test.assert_equals(solve(15000, 20000), 9)
# Test.assert_equals(solve(60000, 70000), 15)
# Test.assert_equals(solve(60000, 130000), 55)


def build_nums():
    nums = {1: ["0", "1", "8"], 2: ["00", "11", "69", "88", "96"]}
    for x in range(3, 5):
        res = []
        building_block = nums[x - 2]
        for num in building_block:
            res.append(f"0{num}0")
            res.append(f"1{num}1")
            res.append(f"6{num}9")
            res.append(f"8{num}8")
            res.append(f"9{num}6")

        nums[x] = res

    final_res = []
    for num, val in nums.items():
        final_res.extend([int(x) for x in val if x[0] != "0" or x == "0"])

    print(sorted(final_res))


build_nums()
