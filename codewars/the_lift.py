"""Code for The Lift problem on Codewars.com."""


class Dinglemouse(object):
    """Class to control elevator."""

    def __init__(self, queues, capacity):
        """Init function."""
        self.capacity = capacity
        self.occupants = []
        self.history = [0]
        self.floor = 0
        self.direction = "up"
        self.queues = queues

    def theLift(self):  # pylint: disable=C0103
        """Start the lift."""
        return None

    def unload(self):
        """Unload passengers."""
        self.occupants = [x for x in self.occupants if x != self.floor]

    def load(self):
        """Load passengers."""
        pass
        # while len(self.occupants) < self.capacity:
        #     self.occupants.append(self.queue.pop(0))

    def stop(self, floor):
        """Stop on floor."""
        self.update_floor(floor)
        self.unload()
        # self.updateDestination()
        self.load()

    def update_floor(self, floor):
        """Update value of current floor."""
        self.history.append(floor)
        self.floor = floor

    def next_stop(self):
        """Get next stop."""
        pass
