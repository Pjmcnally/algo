"""Solution for Codewars problem.

Kyu: 6
Name: Faro Shuffle Count
Link: https://www.codewars.com/kata/57bc802c615f0ba1e3000029

I am pretty sure there is a mathematical solution to this
problem but I cant see the pattern.
"""


def faro_cycles(num):
    """Count required faro shuffles."""
    test_list = list(range(1, num + 1))
    ref_list = test_list[:]

    shuffle_count = 0
    while True:
        shuffle_count += 1
        test_list = shuffle(test_list)
        if test_list == ref_list:
            return shuffle_count


def shuffle(arr):
    """Faro shuffle arbitrary list."""
    t_list = []
    for elem in zip(arr[: len(arr) // 2], arr[len(arr) // 2 :]):
        t_list.extend(elem)

    return t_list
