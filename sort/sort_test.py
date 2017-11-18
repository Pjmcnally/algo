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


def test(mod_name, list_size, repeat, arr_types):
    try:
        module = importlib.import_module(mod_name)
        sorts = inspect.getmembers(module, inspect.isfunction)
    except:
        print("\nModule name not found.  Please enter valid module name")
        return

    if arr_types == "all":
        arr_types = ["srt", "cls", "rnd", "rev"]

    print("\nRunning test on {} module.".format(mod_name))
    print("Using list of length {}. Repeating test {} times.".format(list_size, repeat))

    # sorts is a list of tuples.  Each tuple contians func name and func value.
    for sort_name, sort_func in sorts:
        print("\nTesting {} sorting method:".format(sort_name))
        for arr in arr_types:
            mysetup = (
                # Import, sort and array.
                "from {mod} import {sort};"
                "from lists import {arr}_{num}".format(
                    mod=mod_name,
                    sort=sort_name,
                    arr=arr,
                    num=list_size,
                )
            )
            # Create shallow copy of list or it will be sorted after first run
            # This does introduce a bit of overhead to each test but is necessary
            code = "{sort}({arr}_{num}[:])".format(
                sort=sort_name,
                arr=arr,
                num=list_size
            )
            time = timeit.timeit(
                setup=mysetup,
                stmt=code,
                number=repeat,
            )
            print("Sorting {} took {:.5f}s per run".format(arr, time/repeat))
    return None

if __name__ == '__main__':
    main()
