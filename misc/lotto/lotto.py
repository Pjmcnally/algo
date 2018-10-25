"""Screwing around with simple lottery simulator."""
from math import factorial
from random import randint, sample
from textwrap import dedent


class Lotto():
    """Class to simulate lottery."""

    def __init__(self, config):
        """Init function."""
        self.config = config  # Requires a LottoConfig class object
        self.winning_nums = self.generate_ticket()
        self.odds = self.calculate_odds()
        self.tickets_generated = 0

        # Printing only every 10,000 tickets increases program speed by 5x.
        # Displaying every 10,000 is essentially as fast as not displaying
        # at all. Also very little is gained from increasing interval.
        self.print_interval = (1 if self.odds < 1000000 else 10000)

    def display_start(self):
        """Display winning numbers."""
        print(self.config)
        start = dedent(f"""\

        Winning numbers: {self.winning_nums}
        Odds of winning: 1 in {self.odds:,}

        """)
        print(start)
        print(f"\rTicket counter: {self.tickets_generated:,}", end="")

    def generate_ticket(self):
        """Generate lottery ticket."""
        return LottoTicket(
            choices=self.config.nums,
            num_count=self.config.num_count,
            extra_num_max=self.config.extra_num_max)

    def calculate_odds(self):
        """Calculate odds of winning."""
        total_choices = self.config.num_max - self.config.num_min + 1

        numerator = factorial(total_choices)
        denominator = (factorial(total_choices - self.config.num_count) *
                       factorial(self.config.num_count))
        return (numerator // denominator) * self.config.extra_num_max

    def find_winner(self):
        """Generate tickets to find winners. Stop when desired num found."""
        while True:
            self.tickets_generated += 1
            if self.tickets_generated % self.print_interval == 0:
                print(f"\rTicket counter: {self.tickets_generated:,}", end="")

            if self.generate_ticket() == self.winning_nums:
                break

    def display_end(self):
        """Display final results."""
        print("\r\n\r\nLottery Over!")
        print(f"Tickets required to find winner: {self.tickets_generated:,}")

    def run_lottery(self):
        """Run simulated lottery."""
        self.display_start()
        self.find_winner()
        self.display_end()


class LottoConfig():
    """Hold and parse lottery configuration data."""

    def __init__(self, name, num_min, num_max, num_count, extra_num_max):
        """Init function."""
        self.name = name
        self.num_min = num_min
        self.num_max = num_max
        self.num_count = num_count
        self.nums = range(self.num_min, self.num_max + 1)
        self.extra_num_max = extra_num_max

    def __str__(self):
        """Represent as string."""
        return dedent(f"""\
            Lottery name: {self.name}
            Num range: {self.num_min} - {self.num_max}
            Number of numbers selected: {self.num_count}
            Extra num maximum value: {self.extra_num_max}""")

    @classmethod
    def from_name(cls, name):
        """Generate and return different lottery configurations."""
        if name == "Powerball":
            config = cls(
                name=name,
                num_min=1,
                num_max=69,
                num_count=5,
                extra_num_max=26)
        elif name == "Mega Millions":
            config = cls(
                name=name,
                num_min=1,
                num_max=70,
                num_count=5,
                extra_num_max=25)
        else:  # "Using for testing"
            config = cls(
                name=name,
                num_min=1,
                num_max=50,
                num_count=5,
                extra_num_max=25)

        return config


class LottoTicket():
    """Represent lottery ticket."""

    def __init__(self, choices, num_count, extra_num_max):
        """Init function."""
        self.nums = set(sample(choices, num_count))
        self.extra_num = randint(1, extra_num_max)

    def __eq__(self, other):
        """Test equality."""
        return self.extra_num == other.extra_num and self.nums == other.nums

    def __str__(self):
        """Represent as string."""
        nums = " ".join(f"{x:02}" for x in self.nums)
        return f"{nums} {self.extra_num}"


def main():
    """Execute main function."""
    import os
    os.system('cls')

    # Setup and run lottery
    lottery = Lotto(LottoConfig.from_name("Test"))
    lottery.run_lottery()


if __name__ == '__main__':
    main()
