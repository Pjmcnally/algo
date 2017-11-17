import timeit
import inspect

import bubblesort

from random import shuffle


def main():
    sorts = inspect.getmembers(bubblesort, inspect.isfunction)

    o_arr = list(range(1000))
    s_arr = o_arr[:]
    shuffle(s_arr)

    for name, sort in sorts:
        t_arr = s_arr[:]
        sort(t_arr)

        if t_arr == o_arr:
            print("{} worked".format(name))


if __name__ == '__main__':
    main()


"""
def temp():
    mysetup = "print(sorts)"
        # from bubblesort import {}; from random_lists import {}".format(sort.__name__)
        code = "{}([1, 2, 3])".format(sort.__name__)

    time = timeit.timeit(
            setup=mysetup,
            stmt=code,
            number=100,
            globals=globals()
        )
        print(time)
"""
