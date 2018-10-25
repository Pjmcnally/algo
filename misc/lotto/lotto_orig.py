"""Screwing around with simple lottery simulator.

This file is obsolete and fundamentally flawed. For the new working version see
lotto.py.

The fundamental flaw stems from the fact that I didn't know the order of the
numbers is irrelevant when checking for winners. This files uses an array to
store the numbers. This makes the odds of winning several orders of magnitude
more difficult. This also explains why I wasn't getting any winners on my trial
runs with high numbers.

In the improved version I use a set to store the numbers rendering order
irrelevant. The improved version is also OOP.
"""
from random import randint, sample


def run_lottery():
    """Run simulated lottery."""
    possible_nums = range(1, 71)
    num_count = 5
    extra_max = 25
    counter = 0

    winning_nums = generate_ticket(possible_nums, num_count, extra_max)
    print("\r\nWinning ticket: ", end="")
    print(" ".join(f"{x:02}" for x in winning_nums))
    print(f"\rTickets: {counter:,}", end="")

    while True:
        counter += 1

        # Printing only every 10,000 tickets increases program speed by 5x.
        # Displaying every 10,000 is essentially as fast as not displaying
        # at all. Also very little is gained from increasing interval.
        if counter % 10000 == 0:
            print(f"\rTickets: {counter:,}", end="")
        if generate_ticket(possible_nums, num_count,
                           extra_max) == winning_nums:
            print("\r\n\r\nWinner Found!")
            print(f"Total cost to win: ${counter*2:.2f}")
            break


def generate_ticket(num_options, num_count, extra_max):
    """Generate lottery ticket."""
    ticket = sample(num_options, num_count)
    ticket.append(randint(1, extra_max))

    return ticket


if __name__ == '__main__':
    import os
    os.system('cls')

    run_lottery()
