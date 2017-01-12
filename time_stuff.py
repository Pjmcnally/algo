from timeit import timeit


def tup(string):
    tuple((int(x) for x in string.split(" ")))


def comp(string):
    return [int(x) for x in string.split(" ")]


def for_loop(string):
    results = []
    for x in string.split(" "):
        results.append(int(x))

    return results


def map_func(string):
    return list(map(int, string.split(" ")))


def gen(string):
    return (int(x) for x in string.split(" "))

num_array = list(range(10))
str_array = [str(x) for x in num_array]
num_str = " ".join(str_array)


def main():
    print("comp took ", timeit("comp(num_str)", setup="from __main__ import comp, num_str"))
    print("loop took ", timeit("for_loop(num_str)", setup="from __main__ import for_loop, num_str"))
    print("map  took ", timeit("map_func(num_str)", setup="from __main__ import map_func, num_str"))
    print("gen  took ", timeit("gen(num_str)", setup="from __main__ import gen, num_str"))
    print("tup  took ", timeit("tup(num_str)", setup="from __main__ import tup, num_str"))

if __name__ == '__main__':
    main()
