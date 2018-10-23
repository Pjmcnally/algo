"""Screwing around with simple lottery simulator."""
from random import randint, shuffle


class Lotto():
    """Class to simulate lottery."""

    def __init__(self):
        """Init function."""
        self.nums = list(range(1, 71))
        self.winning_nums = []

    def run_lottery(self):
        """Run simulated lottery."""
        self.winning_nums = self.generate_ticket()
        print("\r\nWinning ticket: {0:02} {1:02} {2:02} {3:02} {4:02} {5:02} ".
              format(*self.winning_nums))

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
        shuffle(self.nums)

        ticket = self.nums[0:5]
        ticket.append(randint(1, 25))

        return ticket


def main():
    """Execute main function."""
    import os
    os.system('cls')

    lottery = Lotto()
    lottery.run_lottery()


if __name__ == '__main__':
    main()
