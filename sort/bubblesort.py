# Bubble sort is a terrible sorting algoright and should only be used for
# learning and mocking


# This is completely unoptimized.
# It will loo
def raw_bubblesort(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1

    return arr

def main():
    arr = [5, 4, 3, 2, 1]
    sort = raw_bubblesort(arr[:])
    print(sort)

main()


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
