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
