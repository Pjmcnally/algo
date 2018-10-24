"""Screwing around with simple lottery simulator."""
from random import randint, shuffle, sample


def run_lottery():
    """Run simulated lottery."""
    winning_nums = generate_ticket()
    print("\r\nWinning ticket: ", end="")
    print(" ".join(f"{x:02}" for x in winning_nums))

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
    num_max = 70
    extra_num_max = 25
    num_selected = 5

    nums = list(range(1, num_max + 1))
    shuffle(nums)

    ticket = nums[0:num_selected]
    ticket.append(randint(1, extra_num_max))

    return ticket


if __name__ == '__main__':
    run_lottery()
