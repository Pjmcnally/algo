from timeit import timeit
from random import shuffle
from bubblesort import raw_bubblesort, shrinking_bubblesort, adaptive_bubblesort

def main():
    sorts = [raw_bubblesort, shrinking_bubblesort, adaptive_bubblesort]

    for sort in sorts:
        time = timeit(
            setup="from bubblesort import {}; from random import shuffle; arr = list(range(100)); shuffle(arr)".format(sort.__name__),
            stmt="{}(arr)".format(sort.__name__),
            number=100
        )
        print(time)


if __name__ == '__main__':
    main()
