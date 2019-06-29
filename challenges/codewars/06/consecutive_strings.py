def longest_consec(strarr, k):
    if len(strarr) < k or len(strarr) == 0 or k <= 0:
        return ""

    max_len, max_i = 0, 0
    length_arr = [len(x) for x in strarr]
    for i, val in enumerate(strarr):
        range_sum = sum(length_arr[i : i + k])
        if range_sum > max_len:
            max_len = range_sum
            max_i = i

    return "".join(strarr[max_i : max_i + k])


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest as Test  # noqa: E402, pylint: disable=E0401


def testing(actual, expected):
    Test.assert_equals(actual, expected)


testing(
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2),
    "abigailtheta",
)
testing(
    longest_consec(
        [
            "ejjjjmmtthh",
            "zxxuueeg",
            "aanlljrrrxx",
            "dqqqaaabbb",
            "oocccffuucccjjjkkkjyyyeehh",
        ],
        1,
    ),
    "oocccffuucccjjjkkkjyyyeehh",
)
testing(longest_consec([], 3), "")
testing(
    longest_consec(
        [
            "itvayloxrp",
            "wkppqsztdkmvcuwvereiupccauycnjutlv",
            "vweqilsfytihvrzlaodfixoyxvyuyvgpck",
        ],
        2,
    ),
    "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck",
)
testing(
    longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2),
    "wlwsasphmxxowiaxujylentrklctozmymu",
)
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
testing(
    longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3),
    "ixoyx3452zzzzzzzzzzzz",
)
testing(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
testing(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
