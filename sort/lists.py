from random import shuffle

def gen_rand_list(arr):
    copy = arr[:]
    shuffle(copy)

    return copy

num = 10

sort = list(range(num))
rand = gen_rand_list(sort)
