from timeit import timeit


def tup(array):
    tuple((x**2 for x in array))


def comp(array):
    return [x**2 for x in array]


def for_loop(array):
    results = []
    for x in array:
        results.append(x**2)

    return results


def map_func(array):
    return list(map(lambda x: x**2, array))


def gen(array):
    return list(x**2 for x in array)

num_array = range(100)


def main():
    print("comp took ", timeit("comp(num_array)", setup="from __main__ import comp, num_array"))
    print("loop took ", timeit("for_loop(num_array)", setup="from __main__ import for_loop, num_array"))
    print("map  took ", timeit("map_func(num_array)", setup="from __main__ import map_func, num_array"))
    print("gen  took ", timeit("gen(num_array)", setup="from __main__ import gen, num_array"))
    print("tup  took ", timeit("tup(num_array)", setup="from __main__ import tup, num_array"))

if __name__ == '__main__':
    main()
