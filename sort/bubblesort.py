"""
Bubble sort is a simple comparative sorting algorithm.

It is very inefficient and should basically never be used.  Other simple sorts
(like insertion or select) should almost alwasy be prefered over bubble.
"""

def raw_bubblesort(arr):
    """
    This version of bubble sort is completely unoptimized.
    It will fully loop over the list (even the "sorted" section every time)
    """
    l = len(arr) - 1
    for loop in range(l):
        for i in range(l):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def shrinking_bubblesort(arr):
    """
    This version of bubble sort is slightly optimized.

    It will only loop over the unsorted section of the list.  After each pass
    we can assume the final element of that pass is sorted and we do not need
    to examine it again.
    """

    # j is our shriking upper bound. i counts from 0 to j. Swap if necessary.
    for j in range(len(arr) - 1, 0, -1):
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def adaptive_bubblesort(arr):
    j = len(arr) - 1  # set upper bound

    # j is our adaptive upper bound. i counts from 0 to j. Swap if necessary.
    while j > 0:
        new_j = 0  # Assume new upperbound in 0 (assume list is sorted)
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                new_j = i  # when a swap is made update new upper bound
        j = new_j

    return arr
