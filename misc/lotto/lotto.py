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

        # Set misc attributes
        self.winning_nums = self.generate_ticket()
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
        while True:
            self.tickets_generated += 1

            # Printing only every 10,000 tickets increases program speed by 5x.
            # Displaying every 10,000 is essentially as fast as not displaying
            # at all. Also very little is gained from increasing interval.
            if self.tickets_generated % 10000 == 0:
                print(f"\rTickets: {self.tickets_generated:012,}", end="")

            if self.generate_ticket() == self.winning_nums:
                break

    def display_end(self):
        """Display final results."""
        print("\r\n\r\nLottery Over!")
        print(f"Tickets required to find winner: {self.tickets_generated:,}")

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
