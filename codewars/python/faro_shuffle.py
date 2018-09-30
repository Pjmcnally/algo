def shuffle(arr):
    t_list = []
    for elem in zip(arr[:len(arr) // 2], arr[len(arr) // 2:]):
        t_list.extend(elem)

    return t_list


def test(num):
    test_list = list(range(1, num + 1))
    ref_list = test_list[:]

    shuffle_count = 0
    while True:
        shuffle_count += 1
        test_list = shuffle(test_list)
        if test_list == ref_list:
            return shuffle_count


def main():
    for x in range(2, 101, 2):
        print("{} requires {} shuffles.".format(x, test(x)))


if __name__ == '__main__':
    main()
