class Dinglemouse(object):
    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.occupants = []
        self.history = [0]
        self.floor = 0
        self.destination = 0
        self.direction = "up"
        self.setQueues(queues)

    def setQueues(self, queues):
        self.up_queue = [[p for p in f if p > i] for i, f in enumerate(queues)]
        self.dn_queue = [[p for p in f if p < i] for i, f in enumerate(queues)]

    def theLift(self):
        return self.up_queue

    def unload(self):
        self.occupants = [x for x in self.occupants if x != self.floor]

    def load(self):
        while len(self.occupants) < self.capacity:
            self.occupants.append(queue.pop(0))

    def stop(self, floor):
        self.updateFloor(floor)
        self.unload()
        self.updateDestination()
        self.load()

    def updateFloor(self, floor):
        self.history.append(floor)
        self.floor = floor

    def nextStop(self):
        pass
