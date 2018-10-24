"""Screwing around with simple lottery simulator."""
from random import randint, sample


class Lotto():
    """Class to simulate lottery."""

    def __init__(self):
        """Init function."""
        # Setup pool of possible numbers
        self.num_max = 70
        self.extra_num_max = 25
        self.nums = range(1, self.num_max + 1)

        # Setup rules to select nums
        self.num_selected = 5
        self.winning_nums = []

    def run_lottery(self):
        """Run simulated lottery."""
        # Generate and display winning numbers
        self.winning_nums = self.generate_ticket()
        print("\r\nWinning ticket: ", end="")
        print(" ".join(f"{x:02}" for x in self.winning_nums))

        # Attempt to match winning numbers. Stop when winning ticket found.
        counter = 0
        while True:
            counter += 1
            print("\rTickets tried: {0:012,}".format(counter), end="")
            if self.generate_ticket() == self.winning_nums:
                print("\r\n\r\nWinner Found!")
                print(f"Total cost to win: ${counter*2:.2f}")
                break

    def generate_ticket(self):
        """Generate lottery ticket."""
        ticket = sample(self.nums, self.num_selected)
        ticket.append(randint(1, self.extra_num_max))

        return ticket


def main():
    """Execute main function."""
    import os
    os.system('cls')

    lottery = Lotto()
    lottery.run_lottery()


if __name__ == '__main__':
    main()
