import random


def generate_list(length, style):
    """Generate list of specific length and style."""
    if style == "sorted":
        return list(range(length))
    elif style == "reverse":
        return list(range(length))[::-1]
    elif style == "random":
        return make_random(length)
    elif style == "almost":
        pass
    elif style == "similar":
        return make_similar(length)


def make_random(length, seed=1):
    """Generate random list of specific length."""
    temp_list = list(range(length))
    random.seed(seed)
    random.shuffle(temp_list)
    return temp_list


def make_close(arr):
    """Generate a randomized list that is almost sorted.

    This function is entirely made up by me.  All of the numbers are guesses.
    I have done some testing and it seems to perform as I want.

    Right now it makes lists where about 20% of the numbers are not where they
    should be.  Those numbers are usually ~3 spots away from their sorted spot.

    As lists get longer the max dist climbs as some number can be moved more
    than once.

    This will fail frequently with small lists.  I recommend use where len >= 100
    """
    temp = arr[:]
    rand_limit = 10
    indx_limit = min(5, int(len(arr) ** 0.5))

    for i, elem in enumerate(temp):
        rand = randint(1, rand_limit)
        if rand == rand_limit:
            diff = randint(1, indx_limit)
            try:
                temp[i], temp[i + diff] = temp[i + diff], temp[i]
            except:
                pass  # if array is out of bounds just skip it.
    return temp


def make_similar(length, seed=1):
    """Generate a randomized list of specified length where all numbers are 1 - 5."""
    temp_list = [1, 2, 3, 4, 5] * (length // 5)
    random.seed(seed)
    random.shuffle(temp_list)
    return temp_list


def check_cls(arr):
    """Check "Closely" randomized list.

    This function checks my close list generating function to see
    what kind of results I am getting.
    """
    num_off = 0
    off = []

    for i, elem in enumerate(arr):
        if elem != i:
            num_off += 1
            off.append(abs(i - elem))

    print("{} total numbers are out of place".format(num_off))
    print("{} is the largest gap between number and place".format(max(off)))
    print(
        "{:.1f} is the average distance a off number is off".format(sum(off) / len(off))
    )
