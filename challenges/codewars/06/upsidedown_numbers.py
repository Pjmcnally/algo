"""Solution for Codewars problem.

Kyu: 6
Name: Upside down numbers
Link: https://www.codewars.com/kata/59f7597716049833200001eb
"""


def solve(a, b):
    """Calculate number of upside down number within given range.

    This is the brute force approach. It checks each number testing if it qualifies.
    """
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


def build_nums():
    """Calculate number of upside down number within given range.

    This is a better approach. It doesn't check any numbers instead it builds possible
    numbers out of the possible pieces.
    """
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

    return len(final_res)


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as Test  # noqa: E402, pylint: disable=E0401

Test.assert_equals(solve(0, 10), 3)
Test.assert_equals(solve(10, 100), 4)
Test.assert_equals(solve(100, 1000), 12)
Test.assert_equals(solve(1000, 10000), 20)
Test.assert_equals(solve(10000, 15000), 6)
Test.assert_equals(solve(15000, 20000), 9)
Test.assert_equals(solve(60000, 70000), 15)
Test.assert_equals(solve(60000, 130000), 55)
