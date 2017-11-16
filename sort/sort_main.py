from random import shuffle
from bubblesort import raw_bubblesort, shrinking_bubblesort, adaptive_bubblesort

def main():
    arr = list(range(100))
    shuffle(arr)

    a_1 = arr[:]
    a_2 = arr[:]
    a_3 = arr[:]

    raw_bubblesort(a_1)
    shrinking_bubblesort(a_2)
    adaptive_bubblesort(a_3)

    if (a_1 == a_2 == a_3):
        print("YAY")

if __name__ == '__main__':
    main()
