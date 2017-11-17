import timeit
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
        temp_arr = lists.rand[:]
        sort(temp_arr)

        if temp_arr == lists.sort:
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
