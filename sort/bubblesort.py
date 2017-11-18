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
    notes (in variable new_j) the position of the last swap.  All elements after
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

def simple_cocktailSort(arr):
    """
    This version of bubble sort works back and forth instead of always starting
    at the beginning.

    It operates like shrinking_bubblesort and will only assume 1 elem sorted per
    pass.  However, if no swaps are made it will stop sorting as the list is
    sorted.

    This is an in-place sort.
    """
    # Assume list is unsorted, set start and end
    swapped = True
    start = 0
    end = len(arr) - 1

    while (swapped==True):
        # Assume list is sorted until swap is made
        swapped = False

        # Loop from left to right same as the bubble sort
        for i in range (start, end):
            if (arr[i] > arr[i + 1]) :
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped=True

        # If nothing moved, then array is sorted.
        if (swapped==False):
            break

        # Assume list is sorted until swap is made
        swapped = False

        # Reduce the end as we know one more element is sorted
        end = end - 1

        # Loop from right to left same as bubble sort
        for i in range(end, start,-1):
            if (arr[i] < arr[i - 1]):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Increase start as we know one more element is sorted
        start = start + 1

    return None

def adaptive_cocktail(arr):
    """
    This version of bubble sort works back and forth instead of always starting
    at the beginning.

    It, like adaptive_bubblesort, will expand the "sorted parts of the list
    depending on the swaps made.  At the beginning of each pass it assumes the
    rest of the list is sorted.  Once a swap is made that position is saved. At
    the end of the pass all elements after that position are sorted.

    This can significantly increase speed on data that is already or almost
    sorted.

    This is an in-place sort.
    """
    end = len(arr) - 1
    beg = 0

    while beg < end:
        new_end = 0
        for i in range(beg, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                new_end = i  # when a swap is made update new upper bound
        end = new_end

        if end <= beg:
            break

        new_beg = len(arr) - 1
        for i in range(end, beg, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                new_beg = i  # when a swap is made update new upper bound
        beg = new_beg

    return None
