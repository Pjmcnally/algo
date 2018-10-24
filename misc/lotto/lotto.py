"""Screwing around with simple lottery simulator."""
from random import randint, sample


class Lotto():
    """Class to simulate lottery."""

    def __init__(self):
        """Init function."""
        # Setup pool of possible numbers
        self.num_max = 70
        self.num_selected = 5
        self.nums = range(1, self.num_max + 1)
        self.extra_num_max = 25

        # Get winning numbers
        self.winners = 0
        self.winners_wanted = 1
        self.winning_nums = self.generate_ticket()

        # Set
        self.tickets_generated = 0

    def generate_ticket(self):
        """Generate lottery ticket."""
        ticket = sample(self.nums, self.num_selected)
        ticket.append(randint(1, self.extra_num_max))

        return ticket

    def display_start(self):
        """Display winning numbers."""
        print("\r\nWinning ticket: ", end="")
        print(" ".join(f"{x:02}" for x in self.winning_nums))

    def find_winners(self):
        """Generate tickets to find winners. Stop when desired num found."""
        while self.winners < self.winners_wanted:
            self.tickets_generated += 1
            if self.generate_ticket() == self.winning_nums:
                self.winners += 1

            print(
                "\rTickets tried: {0:012,}. Winners found: {1:,}".format(
                    self.tickets_generated, self.winners),
                end="")

    def display_end(self):
        """Display final results."""
        print("\r\n\r\nLottery Over!")
        print("Average tickets per winner: {0:,}".format(
            self.tickets_generated // self.winners))

    def run_lottery(self):
        """Run simulated lottery."""
        self.display_start()
        self.find_winners()
        self.display_end()


def main():
    """Execute main function."""
    import os
    os.system('cls')

    lottery = Lotto()
    lottery.run_lottery()


if __name__ == '__main__':
    main()
