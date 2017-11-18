from random import shuffle, sample, randint
import lists

def make_close(arr):
    """
    This function is entirely made up by me.  All of the numbers are guesses.
    I have done some testing and it seems to perform as I want.d

    Right now it makes lists where about 20% of the numbers are not where they
    should be.  Those numbers are usually ~3 spots away from their sorted spot.

    As lists get longer the max dist climbs as some number can be moved more
    than once.

    This will fail freqently with small lists.  I recomend use where len >= 100
    """

    temp = arr[:]
    rand_limit = 10
    indx_limit = min(5, int(len(arr)**.5))

    for i, elem in enumerate(temp):
        rand = randint(1, rand_limit)
        if (rand == rand_limit):
            diff = randint(1, indx_limit)
            try:
                temp[i], temp[i + diff] = temp[i + diff], temp[i]
            except:
                pass # if array is out of bounds just skip it.
    return temp

def gen_lists(file, num):
    """ Generates lists of differnt types and writes to temp file"""

    srt_list = list(range(num))  # Generates ordered list
    rev_list = srt_list[::-1]  # Generates reversed list
    rnd_list = sample(srt_list, len(srt_list))  # Generates random list (without modifying original)
    cls_list = make_close(srt_list)  # Generates mostly sorted list

    with open(file, "w") as f:
        f.write("srt_{} = {}\n".format(num, srt_list))
        f.write("rev_{} = {}\n".format(num, rev_list))
        f.write("cls_{} = {}\n".format(num, cls_list))
        f.write("rnd_{} = {}\n".format(num, rnd_list))

def check_cls(arr):
    """
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
    print("{:.1f} is the average distance a off number is off".format(sum(off)/len(off)))

def main():
    file = "list.txt"
    num = 1000
    gen_lists(file, num)

    for x in [lists.cls_100, lists.cls_1000, lists.cls_10000, lists.cls_100000]:
        check_cls(x)

if __name__ == '__main__':
    main()
