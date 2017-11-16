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


def bubblesort(arr):
    swapped = False
    j = len(arr) - 2
    while not swapped:
        for i, val in enumerate(arr[:j]):
            if val > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        j -= 1
    return arr

def main():
    arr = [5, 4, 3, 2, 1]
    raw_bubblesort(arr)
    print(arr)

if __name__ == '__main__':
    main()
