"""Code for The Lift on Codewars.com.

https://www.codewars.com/kata/the-lift
"""
import codewarstest


class Dinglemouse(object):
    """Class to control elevator."""

    def __init__(self, people, capacity):
        """Init function."""
        self.capacity = capacity
        self.occupants = []
        self.history = [0]
        self.floor = 0
        self.direction = "up"
        self.queues = list(people)
        self.stops = set()

    def theLift(self):  # pylint: disable=C0103
        """Start the lift."""
        while self.check_waiting():  # while anyone is waiting
            self.build_stops()  # Add people waiting to stops
            while self.stops:  # Go one direction until done
                self.stop(self.get_next_stop())
            self.change_direction()

        if self.floor:  # Done. If not on 0 go to 0.
            self.history.append(0)

        return self.history

    def check_waiting(self):
        """Check to see if anyone is waiting."""
        if [x for x in self.queues if x]:
            return True
        else:
            return False

    def change_direction(self):
        """Change direction."""
        if self.direction == 'up':
            self.direction = 'dn'
        elif self.direction == 'dn':
            self.direction = 'up'

    def unload(self):
        """Unload passengers."""
        self.occupants = [x for x in self.occupants if x != self.floor]

    def load(self):
        """Load passengers."""
        temp_list = []

        if self.direction == 'up':
            for elem in self.queues[self.floor]:
                if len(self.occupants) < self.capacity and elem > self.floor:
                    self.occupants.append(elem)
                    self.stops.add(elem)
                else:
                    temp_list.append(elem)
        elif self.direction == 'dn':
            for elem in self.queues[self.floor]:
                if len(self.occupants) < self.capacity and elem < self.floor:
                    self.occupants.append(elem)
                    self.stops.add(elem)
                else:
                    temp_list.append(elem)

        self.queues[self.floor] = temp_list

    def stop(self, floor):
        """Stop on floor."""
        self.update_floor(floor)
        self.unload()
        self.load()
        self.stops.remove(self.floor)

    def update_floor(self, floor):
        """Update value of current floor."""
        if self.floor != floor:
            self.history.append(floor)
            self.floor = floor

    def get_next_stop(self):
        """Get next stop."""
        if self.direction == 'up':
            return min(self.stops)
        elif self.direction == 'dn':
            return max(self.stops)

    def build_stops(self):
        """Get floors with people waiting for elevator in current direction."""
        if self.direction == 'up':
            for i, elem in enumerate(self.queues):
                if [x for x in elem if x > i]:
                    self.stops.add(i)
        elif self.direction == 'dn':
            for i, elem in enumerate(self.queues):
                if [x for x in elem if x < i]:
                    self.stops.add(i)


# Tests below this line
# ==============================================================================
tests = [
    [((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0]],
    [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0]],
    [((), (3, ), (4, ), (), (5, ), (), ()), [0, 1, 2, 3, 4, 5, 0]],
    [((), (0, ), (), (), (2, ), (3, ), ()), [0, 5, 4, 3, 2, 1, 0]],
]

for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    codewarstest.assert_equals(lift.theLift(), answer)
