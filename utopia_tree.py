from timeit import timeit
array = range(10)


def linear_while(array):
    def growth_calc(n):
        height = 1
        for x in range(1, n+1):
            if x % 2 == 0:
                height += 1
            else:
                height *= 2
        return height

    for val in array:
        growth_calc(val)

    return True


def recursive(array):
    def growth_calc(n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return growth_calc(n-1) + 1
        else:
            return growth_calc(n-1) * 2

    for val in array:
        growth_calc(val)

    return True


def line_2_o1(array):
    pass


def line_1_o1(array):
    def growth_calc(n):
        mod = n % 2
        return int((2 ** ((n + (mod)) / 2 + 1)) - 1 - (mod))

    for val in array:
        growth_calc(val)

    return True


def test(name):
    val = timeit("{}".format(name + "(array)"),
                 setup="from __main__ import {}, array".format(name),
                 number=1000)
    return name, val


def main():
    func_list = ["linear_while", "recursive", "line_2_o1", "line_1_o1"]
    for x in func_list:
        name, val = test(x)
        print("{} took {}".format(name, val))


main()
