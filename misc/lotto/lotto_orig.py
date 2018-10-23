"""Screwing around with simple lottery simulator."""
from random import randint, shuffle


def run_lottery():
    """Run simulated lottery."""
    winning_nums = generate_ticket()
    print("\r\nWinning ticket: {0:02} {1:02} {2:02} {3:02} {4:02} {5:02} ".
          format(*winning_nums))

    counter = 0
    while True:
        counter += 1
        print("\rTickets tried: {0:012,}".format(counter), end="")
        if generate_ticket() == winning_nums:
            print("\r\n\r\nWinner Found!")
            print(f"Total cost to win: ${counter*2:.2f}")
            break


def generate_ticket():
    """Generate lottery ticket."""
    nums = list(range(1, 71))
    shuffle(nums)

    ticket = nums[0:5]
    ticket.append(randint(1, 25))

    return ticket


if __name__ == '__main__':
    run_lottery()
