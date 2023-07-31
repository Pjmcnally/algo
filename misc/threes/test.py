import time
import datetime
import argparse

def count_triple_threes(start, stop):
    count = 0
    for num in range(start, stop, 2):
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
    # Parse Args
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-d", "--digits", help="Digit Count")
    args = argParser.parse_args()
    digits = int(args.digits)
    print(f"Digit Count: {digits}")
    print(f"starting: {datetime.datetime.now()}")
    start = time.time()
    count = count_triple_threes(10**(digits - 1), 10**digits)
    end = time.time()
    print(f"Complete: {datetime.datetime.now()}")

    duration = datetime.timedelta(seconds = end - start)
    print(f"Duration: {duration}")

    print(f"Count: {count}")

main()
