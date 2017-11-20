def insertion_swap_sort(arr):
    """
    Inserton sort is a simple sorting algorithm.

    This implementation loops over a list n-1 times.

    The first loop begins with the second element as the first element is
    assumed to be sorted.  Examining the second element swap it to the left
    if the element to the left is larger.  Do this until the element is in the
    correct position.

    Repeat this procedure until all elements are sorted.

    This is an in-place and stable sort.

    However, the significant amount of swaps can have a negative impact on its
    runtime
    """
    for i in range(1, len(arr)):
        j = i
        while (j > 0 and arr[j - 1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def insertion_sort(arr):
    """
    Inserton sort is a simple sorting algorithm.

    Insertion sort loops of the list n-1 times.  The first loop assumes the first
    element is sorted.  The second element is then put into its proper place
    in the sorted section of the list.

    This continues until all elements are sorted.

    """
    for i in range(1, len(arr)):
        val = arr[i]
        pos = i
        while (pos > 0 and arr[pos - 1] > val):
            arr[pos] = arr[pos - 1]
            pos -= 1

        arr[pos] = val

def selection_sort(arr):
    """
    Selection sort is a simple sorting algorithm.

    Loop over the list n - 1 times (where n is the len of the list). Each time
    find the smallest item in the list and swap it with the first unsorted item
    in the list.  Each pass 1 more item will be sorted.
    """
    for i in range(len(arr) - 1):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

def cocktail_selection(arr):
    """
    Cocktail selection sort works like cocktail bubble sort.

    In a normal selection sort each pass over the list you find the min (or max)
    value and place it at the beginning (or end) of list.  Each pass sorts 1
    item.

    Cocktail selection sorts find both the min and max values and places both
    at the beginning and end respectively.  This should reduce the total loops
    required over the list by 1/2 as 2 items are sorted per pass.
    """
    n = len(arr)
    for i in range(n//2):
        min_i = i
        max_i = i
        for j in range(i + 1, n - i):
            if arr[j] < arr[min_i]:
                min_i = j
            elif arr[j] > arr[max_i]:
                max_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]
        if i == max_i:
            max_i = min_i
        arr[n - 1 - i], arr[max_i] = arr[max_i], arr[n - 1 - i]

# from random import shuffle
# def main():
#     a = []
#     b = [1]
#     c = [2, 1]
#     d = list(range(0, 10))
#     e = list(range(0, 11))
#     shuffle(d)
#     shuffle(e)

#     lists = [a, b, c, d, e]
#     for l in lists:
#         selection_sort(l)

#     assert a == []
#     assert b == [1]
#     assert c == [1, 2]
#     assert d == list(range(10))
#     assert e == list(range(11))


# main()
