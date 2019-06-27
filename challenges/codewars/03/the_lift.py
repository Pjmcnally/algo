"""Solution for Codewars problem.

Kyu: 3
Name: The Lift
Link: https://www.codewars.com/kata/58905bfa1decb981da00009e
"""
import operator


class Dinglemouse(object):
    """Class to control elevator."""

    # 1 is going up, 0 is going down.
    DIR_FUNC = {1: operator.gt, 0: operator.lt}

    def __init__(self, floors, capacity):
        """Init function."""
        self.capacity = capacity
        self.occupants = []
        self.history = [0]
        self.floor = 0
        self.direction = 1  # 1 is up, 0 is down.
        self.queues = [list(floor) for floor in floors]
        self.stops = set()

    def theLift(self):  # pylint: disable=C0103
        """Start the lift."""
        while self.check_for_waiting():  # while anyone is waiting
            self.build_stops()  # Add people waiting to go current dir to stops
            while self.stops:  # Continue until no stops remain
                self.stop(self.get_next_stop())  # Stop at next stop
            self.change_direction()  # Change direction when stops is empty

        self.update_floor(0)  # Done. Got to the bottom floor.

        return self.history

    def check_for_waiting(self):
        """Check to see if anyone is waiting."""
        for floor in self.queues:
            if floor:
                return True

        return False

    def change_direction(self):
        """Change direction."""
        self.direction = int(not self.direction)

    def unload(self):
        """Unload passengers."""
        self.occupants = [x for x in self.occupants if x != self.floor]

    def load(self):
        """Load passengers."""
        temp_list = []

        for person in self.queues[self.floor]:
            if (
                len(self.occupants) < self.capacity  # If there is room
                # and someone going the direction of the lift.
                and self.DIR_FUNC[self.direction](person, self.floor)
            ):
                self.occupants.append(person)
                self.stops.add(person)
            else:
                temp_list.append(person)  # Save remaining people to leave

        self.queues[self.floor] = temp_list  # Replace orig list with remaining

    def stop(self, floor):
        """Stop on floor."""
        self.update_floor(floor)
        self.unload()
        self.load()

    def update_floor(self, floor):
        """Update value of current floor."""
        if self.floor != floor:
            self.history.append(floor)
            self.floor = floor

        if floor in self.stops:
            self.stops.remove(floor)

    def get_next_stop(self):
        """Get next stop."""
        if self.direction:  # if going up.
            return min(self.stops)  # return lowest stop in the list
        else:  # Going down
            return max(self.stops)  # return highest stop in the list

    def build_stops(self):
        """Get floors with people waiting for elevator in current direction."""
        for i, elem in enumerate(self.queues):
            if [x for x in elem if self.DIR_FUNC[self.direction](x, i)]:
                self.stops.add(i)


# Tests below this line
# ==============================================================================
import os, sys  # noqa: E401, E402

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import codewarstest  # noqa: E402, pylint: disable=E0401

tests = [
    [((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0]],
    [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0]],
    [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0]],
    [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0]],
]

for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    codewarstest.assert_equals(lift.theLift(), answer)
