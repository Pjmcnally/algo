from random import shuffle
from bubblesort import raw_bubblesort, shrinking_bubblesort, adaptive_bubblesort

def main():
    sorts = [raw_bubblesort, shrinking_bubblesort, adaptive_bubblesort]
    o_arr = list(range(1000))
    s_arr = o_arr[:]
    shuffle(s_arr)

    for sort in sorts:
        t_arr = s_arr[:]
        sort(t_arr)

        if t_arr == o_arr:
            print("{} worked".format(sort.__name__))

if __name__ == '__main__':
    main()
