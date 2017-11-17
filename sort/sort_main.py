import timeit
import cProfile
import inspect

import lists
import bubblesort


from random import shuffle

# TODO: generate lists in random_lists module to test against the same list
# TODO: modularize maine so I can specify module or list to test
# TODO: make timeit work

def main():
    sorts = inspect.getmembers(bubblesort, inspect.isfunction)

    for name, sort in sorts:
        mysetup = "from bubblesort import {0}; from lists import {1}; arr = {2}[:]".format(name, "r_100, s_100", "s_100")
        code = "{}(arr)".format(name)
        runs = 10000

        time = timeit.timeit(
                setup=mysetup,
                stmt=code,
                number=runs,
            )
        print("{} took {:.5f}s per run".format(name, time/runs))


if __name__ == '__main__':
    main()
