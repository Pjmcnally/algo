import time
import datetime
import argparse

def count_triple_threes(start, stop):
    # Count all even numbers containing three 3's between two numbers.
    # Provided "start" must be even.
    # TODO Add test that start is even
    count = 0
    for num in range(start, stop, 2):
        if (test_for_three_threes_mod(num)):
            count += 1

    return count

def test_for_three_threes_mod(num):
    # Test if a provided number contains three 3's (they do not need to be adjacent)
    three_count = 0
    while (num > 0):
        if (num % 10) == 3:
            three_count += 1
            if three_count >= 3:
                return True
        num //= 10

    return False

def main():
    # Parse Args
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-d", "--digits", help="Digit Count")
    args = argParser.parse_args()
    digits = int(args.digits)

    # Start log output
    print("")
    print(f"Digit Count: {digits}")
    print(f"starting: {datetime.datetime.now()}")

    # Run calculation w/timer
    start = time.time()
    count = count_triple_threes(10**(digits - 1), 10**digits)
    end = time.time()

    # Finish log output
    print(f"Complete: {datetime.datetime.now()}")
    print(f"Duration: {datetime.timedelta(seconds = end - start)}")
    print(f"Count: {count}")


main()
