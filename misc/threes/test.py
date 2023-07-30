import time
import datetime

def count_triple_threes(start, stop):
    count = 0
    for num in range(start, stop):
        if (test_for_three_threes_mod(num)):
            count += 1

    return count

def test_for_three_threes_mod(num):
    three_count = 0
    while (num > 0):
        if (num % 10) == 3:
            three_count += 1
        num //= 10

    return three_count >= 3

def main():
    print(f"starting: {datetime.datetime.now()}")
    start = time.time()

    count = count_triple_threes(1000000000, 10000000000)

    end = time.time()
    print(f"Complete: {datetime.datetime.now()}")

    duration = datetime.timedelta(seconds = end - start)
    print(f"Duration: {duration}")

    print(f"Count: {count}")

main()
