def insertion_sort(arr):
    """Inserton sort"""
    pass

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
