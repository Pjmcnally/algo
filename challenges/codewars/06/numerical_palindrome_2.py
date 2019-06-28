"""Solution for Codewars problem.

Kyu: 6
Name: Numerical Palindrom #2
Link: https://www.codewars.com/kata/58de819eb76cf778fe00005c
"""


def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"

    str_num = str(num)
    # All Palendromes must have the following patterns: xox xx at the middle.
    # Just test for those patterns. If found return true.
    for i, char in enumerate(str_num[: len(str_num) - 1]):
        if char == str_num[i + 1]:  # test for matching consecutive letters
            return True
        if i + 2 < len(str_num) and char == str_num[i + 2]:  # Text for xox pattern
            return True

    return False


# def palindrome(num):
#     if not isinstance(num, int) or num < 0:
#         return "Not valid"

#     str_num = str(num)
#     # Brute force approach. Test all numbers until list is desired size.
#     for i, let in enumerate(str_num):
#         for j in range(1, len(str_num) - i + 1):
#             if test_palindrom(str_num[i : j + i]):
#                 return True

#     return False


# def test_palindrom(num):
#     if len(num) < 2:
#         return False

#     str_num = str(num)
#     i, j = 0, len(str_num) - 1

#     while i < j:
#         if str_num[i] == str_num[j]:
#             i += 1
#             j -= 1
#         else:
#             return False

#     return True


palindrome(868)
