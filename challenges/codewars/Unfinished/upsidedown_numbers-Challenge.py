"""Solution file for https://www.codewars.com/kata/upside-down-numbers-challenge-edition/train/python."""  # noqa: E501


def build_nums(a, b):
    """Create list of upside down numbers."""
    nums = {1: ["0", "1", "8"], 2: ["00", "11", "69", "88", "96"]}
    digit_count = len(b)

    for x in range(max(nums.keys()) + 1, digit_count + 1):
        res = []
        building_block = nums[x - 2]
        for num in building_block:
            res.append(f"0{num}0")
            res.append(f"1{num}1")
            res.append(f"6{num}9")
            res.append(f"8{num}8")
            res.append(f"9{num}6")

        nums[x] = res

    count = 0
    for val in nums.values():
        for num in val:
            if num[0] == "0":
                continue
            elif len(a) < len(num) < len(b):
                count += 1
            elif len(a) == len(num) and a < num:
                count += 1
            elif len(b) == len(num) and b > num:
                count += 1

    if a == "0":
        count += 1

    return count


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as test  # noqa: E402, pylint: disable=E0401

test.describe("Example Tests")
test.assert_equals(build_nums("0", "10"), 3)
test.assert_equals(build_nums("10", "100"), 4)
test.assert_equals(build_nums("100", "1000"), 12)
test.assert_equals(build_nums("1000", "10000"), 20)
test.assert_equals(build_nums("10000", "100000"), 60)
test.assert_equals(build_nums("100000", "1000000"), 100)
test.assert_equals(build_nums("1000000", "10000000"), 300)
test.assert_equals(build_nums("10000000", "100000000"), 500)
test.assert_equals(build_nums("100000000", "1000000000"), 1500)
