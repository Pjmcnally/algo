import inspect
import importlib
import timeit
import sys

# TODO: generate lists in random_lists module to test against the same list
# TODO: modularize maine so I can specify module or list to test
# TODO: make timeit work

def main(mod_name, list_size=1000, runs=10):
    module = importlib.import_module(mod_name)
    sorts = inspect.getmembers(module, inspect.isfunction)
    arr_types = ["srt", "cls", "rnd", "rev"]

    for sort_name, sort_func in sorts:
        print("\nTesting {} sorting method:".format(sort_name))
        for arr in arr_types:
            mysetup = (
                # Import, sort and array.
                "from {mod} import {sort};"
                "from lists import {arr}_{num};"
                # Make shallow copy of array each setup or it will become sorted
                "arr = {arr}_{num}[:];".format(
                    mod=module.__name__,
                    sort=sort_name,
                    arr=arr,
                    num=list_size,
                )
            )
            # Use shallow copy arr created in setup above
            code = "{sort}(arr)".format(sort=sort_name)
            time = timeit.timeit(
                setup=mysetup,
                stmt=code,
                number=runs,
            )
            print("Sorting {} took {:.5f}s per run".format(arr, time/runs))

if __name__ == '__main__':
    main("bubblesort")
