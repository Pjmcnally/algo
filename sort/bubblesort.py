"""
Bubble sort is a simple comparative sorting algorithm.

It is very inefficient and should basically never be used.  Other simple sorts
(like insertion or select) should almost always be preferred over bubble sort.

Bubble sort loops over the array, compares adjacent elements, and swaps
them if they are out of order.  This is repeated until the list is sorted.

Worst case this will require n^2 runtime.  For unoptimized Bubble sorts it will
always require n^2 runtime.

It is possible to optimize bubble sort slightly by looping over a smaller and
smaller section of the list each pass.  After one loop the last element of the
list is guaranteed to be sorted and no longer needs to be considered.

It is possible to take this approach a step futher and adaptively expand the
sorted section of the list by noting the position of the last swap.  This can
significantly speed up bubble sort especially on data that is already or almost
sorted.
"""
""" Testing Results:
Running test on bubblesort module.
Test is using all list types
Test is using list of length 10,000.
Each test is repeated 10 times.

Testing raw_bubblesort sorting method:
Sorting srt took 12.18884s per run
Sorting cls took 12.02357s per run
Sorting rnd took 17.90868s per run
Sorting rev took 23.74025s per run

Testing shrinking_bubblesort sorting method:
Sorting srt took 6.01435s per run
Sorting cls took 6.03654s per run
Sorting rnd took 11.71965s per run
Sorting rev took 17.72745s per run

Testing adaptive_bubblesort sorting method:
Sorting srt took 0.00122s per run
Sorting cls took 0.01712s per run
Sorting rnd took 12.16969s per run
Sorting rev took 18.31845s per run

Testing simple_cocktailSort sorting method:
Sorting srt took 0.00124s per run
Sorting cls took 0.00968s per run
Sorting rnd took 10.23367s per run
Sorting rev took 18.03637s per run

Testing adaptive_cocktail sorting method:
Sorting srt took 0.00125s per run
Sorting cls took 0.00809s per run
Sorting rnd took 9.55495s per run
Sorting rev took 17.80244s per run

Total process took 0:32:27.271671
"""


def raw_bubblesort(arr):
    """Raw bubble sort.

    This implementation of bubble sort is completely unoptimized. It will fully
    loop over the list (even the "sorted" section every pass).

    This is an in-place sort.
    """
    for loop in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def shrinking_bubblesort(arr):
    """Slightly optimized version of bubble.

    It will only loop over the unsorted section of the list.  After each pass
    we can assume the final element of that pass is sorted and we do not need
    to examine it again.

    This is an in-place sort.
    """
    # j is our shrinking upper bound. i counts from 0 to j. Swap if necessary.
    for j in range(len(arr) - 1, 0, -1):
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def adaptive_bubblesort(arr):
    """Adaptive version of bubble sort.

    At the begining of each pass we assume the rest of the list is sorted and
    notes (in variable new_j) the position of the last swap.  All elements
    after that position are sorted and do not need to be considered.

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
    """Simple cocktail shaker sort.

    This version of bubble sort works back and forth instead of always starting
    at the beginning.

    It operates like shrinking_bubblesort and will only assume 1 elem sorted
    per pass.  However, if no swaps are made it will stop sorting as the list
    is sorted.

    This is an in-place sort.
    """
    # Assume list is unsorted, set beginning and end
    swapped = True
    beg = 0
    end = len(arr) - 1

    while swapped:
        # Assume list is sorted until swap is made
        swapped = False

        # Loop over list from beginning to end, swap if necessary
        for i in range(beg, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If nothing moved, then array is sorted.
        if not swapped:
            break

        # Assume list is sorted until swap is made
        swapped = False

        # Reduce the end as we know one more element is sorted
        end = end - 1

        # Loop from right to left same as bubble sort
        for i in range(end, beg, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Increase beg as we know one more element is sorted
        beg = beg + 1


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
    # Set beginning and end
    beg = 0
    end = len(arr) - 1

    while beg < end:
        # Assume list is sorted until swap is made
        new_end = 0

        # Loop over list from beginning to end, swap if necessary
        for i in range(beg, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                new_end = i  # when a swap is made update new upper bound
        end = new_end

        # if the end is smaller than beginning then list is sorted.
        if end <= beg:
            break

        new_beg = len(arr) - 1
        for i in range(end, beg, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                new_beg = i  # when a swap is made update new upper bound
        beg = new_beg

    return None
