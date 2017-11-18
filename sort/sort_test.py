import argparse
import inspect
import importlib
import timeit

def main():
    parser = argparse.ArgumentParser(description="Test sorting module displaying timed results.")

    # Add required argument "module name"
    parser.add_argument(
        "mod_name",
        help="The module you wish to test.",
        type=str
    )

    # Add optional argument "list size"
    parser.add_argument(
        "-l",
        "--list_size",
        help="The size of list to test with. Default = 1000.",
        choices=[100, 1000, 10000, 100000],
        default=1000,
        type=int
    )

    # Add option argument "repeat"
    parser.add_argument(
        "-r",
        "--repeat",
        help="The number or times to repeat each test. Default = 3.",
        default=3,
        type=int
    )

    # Add optional argument "array types"
    parser.add_argument(
        "-t",
        "--type",
        help="The types of array(s) to test with. Default = all.",
        choices=["all", "srt", "cls", "rnd", "rev"],
        default="all",
        type=str
    )

    # Parse argument and run test with provided arguements
    args = parser.parse_args()
    print(args.type)
    test(args.mod_name, args.list_size, args.repeat, args.type)

    return None


def test(mod_name, list_size, repeat, arr):
    try:
        module = importlib.import_module(mod_name)
        sorts = inspect.getmembers(module, inspect.isfunction)
    except:
        print("\nModule name not found.  Please enter valid module name")
        return

    if arr == "all":
        arr_types = ["srt", "cls", "rnd", "rev"]
    else:
        arr_types = []
        arr_types.append(arr)

    print(
        "\nRunning test on {mod} module."
        "\nTest is using {type} list types"
        "\nTest is using list of length {size:,}."
        "\nEach test is repeated {rep:,} times.".format(
            mod=mod_name,
            size=list_size,
            rep=repeat,
            type=arr
        )
    )

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
