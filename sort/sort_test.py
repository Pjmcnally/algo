import inspect
import importlib
import timeit
import sys

# TODO: generate lists in random_lists module to test against the same list
# TODO: modularize maine so I can specify module or list to test
# TODO: make timeit work

def main():
    # This whole function is super kludgy and needs significant work.
    # Right now it works for me so I am leaving it alone.
    if len(sys.argv) == 1:
        print("\nArguments required.  Please provide a module to test.")
        return
    elif len(sys.argv) == 2:
        test(sys.argv[1])
    elif len(sys.argv) == 5:
        mod_name = sys.argv[1]
        try:
            list_size = int(sys.argv[2])
            runs = int(sys.argv[3])
        except:
            print("\nlist_size and runs must both be ints.")
            return
        arr_types = sys.argv[4].split(' ')

        test(mod_name, list_size, runs, arr_types)
    return None


def test(mod_name, list_size=1000, runs=10, arr_types=["srt", "cls", "rnd", "rev"]):
    try:
        module = importlib.import_module(mod_name)
        sorts = inspect.getmembers(module, inspect.isfunction)
    except:
        print("\nModule name not found.  Please enter valid module name")
        return

    # sorts is a list of tuples.  Each tuple contians func name and func value.
    for sort_name, sort_func in sorts:
        print("\nTesting {} sorting method:".format(sort_name))
        for arr in arr_types:
            mysetup = (
                # Import, sort and array.
                "from {mod} import {sort};"
                "from lists import {arr}_{num};"
                # Make shallow copy of array each setup or it will become sorted
                "arr = {arr}_{num}[:];".format(
                    mod=mod_name,
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
    main()
