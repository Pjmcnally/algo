"""Screwing around with simple lottery simulator."""
from random import randint, sample


def run_lottery():
    """Run simulated lottery."""
    possible_nums = range(1, 71)
    num_count = 5
    extra_max = 25

    winning_nums = generate_ticket(possible_nums, num_count, extra_max)
    print("\r\nWinning ticket: ", end="")
    print(" ".join(f"{x:02}" for x in winning_nums))

    counter = 0
    while True:
        counter += 1
        print("\rTickets tried: {0:012,}".format(counter), end="")
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
