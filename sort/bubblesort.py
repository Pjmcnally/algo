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
