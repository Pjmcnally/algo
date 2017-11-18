"""
Bubble sort is a simple comparative sorting algorithm.

It is very inefficient and should basically never be used.  Other simple sorts
(like insertion or select) should almost always be prefered over bubble sort.

Bubble sort loops over the array, compares adjacent elements, and swapps
them if they are out of order.  This is repeated until the list is sorted.

Worst case this will require n^2 runtime.  For unoptimized Bubble sorts it will
always require n^2 runtime.

It is possible to optimize bubble sort slightly by looping over a smaller and
smaller section of the list each pass.  After one loop the last element of the
list is guarenteed to be sorted and no longer needs to be considered.

It is possible to take this approach a step futher and adaptively expand the
sorted section of the list by noting the position of the last swap.  This can
significantly speed up bubble sort espescially on data that is already or almost
sorted.
"""

def raw_bubblesort(arr):
    """
    This implementation of bubble sort is completely unoptimized. It will fully
    loop over the list (even the "sorted" section every pass).

    This is an in-place sort.
    """
    l = len(arr) - 1
    for loop in range(l):
        for i in range(l):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return None

def shrinking_bubblesort(arr):
    """
    This version of bubble sort is slightly optimized.

    It will only loop over the unsorted section of the list.  After each pass
    we can assume the final element of that pass is sorted and we do not need
    to examine it again.

    This is an in-place sort.
    """

    # j is our shriking upper bound. i counts from 0 to j. Swap if necessary.
    for j in range(len(arr) - 1, 0, -1):
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return None

def adaptive_bubblesort(arr):
    """
    This version of bubble sort is significantly optimized.

    At the begining of each pass we assume the rest of the list is sorted and
    note (in variable new_j) the position of the last swap.  All elements after
    that position are sorted and do not need to be considered.

    This can significantly increase speed on data that is already or almost
    sorted.

    This is an in-place sort.
    """
    # j is our upper bound. For the first pass we examine the whole list
    j = len(arr) - 1

    # i counts from 0 to j. Swap elems if necessary.
    while j > 0:
        new_j = 0  # Assume new upperbound is 0 (assume list is sorted)
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                new_j = i  # when a swap is made update new upper bound
        j = new_j

    return None
