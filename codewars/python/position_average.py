from collections import Counter


def pos_average(s):
    nums = s.split(", ")
    s_len = len(nums[0])

    matches = 0
    total_pos = (len(nums) * (len(nums) - 1) // 2) * s_len
    for i in range(s_len):
        c = Counter()
        for elem in nums:
            c[elem[i]] += 1

        for val in c.values():
            if val > 1:
                matches += (val * (val - 1)) // 2

    return matches / total_pos * 100


# Tests below this line
# ==============================================================================
import codewarstest  # noqa: E402, pylint: disable=C0413

codewarstest.assert_equals(
    pos_average("6900690040, 4690606946, 9990494604"), (4 / 15) * 100)
codewarstest.assert_equals(
    pos_average(
        "466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"
    ), (4 / 15) * 100)
codewarstest.assert_equals(
    pos_average(
        "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"
    ), 29.2592592593)
