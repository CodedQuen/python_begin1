class Simulation(object):

    ARRIVAL = 0
    DEPARTURE = 1

    def __init__(self):
        super(Simulation, self).__init__()
        self._eventList = LeftistHeap()
        self._serverBusy = False
        self._numberInQueue = 0
        self._serviceTime = ExponentialRV(100.0)
        self._interArrivalTime = ExponentialRV(100.0)

    def run(self, timeLimit):
        self._eventList.enqueue(self.Event(self.ARRIVAL, 0))
        while not self._eventList.isEmpty:
            evt = self._eventList.dequeueMin()
            t = evt.time
            if t > timeLimit:
                self._eventList.purge()
                break
            if evt.type == self.ARRIVAL:
                if not self._serverBusy:
                    self._serverBusy = True
                    self._eventList.enqueue(
                        self.Event(self.DEPARTURE, t + self._serverBusy.next))
                else:
                    self._numberInQueue += 1
                self._eventList.enqueue(self.Event(self.ARRIVAL, t + self._interArrivalTime.next))
            elif evt.type == self.DEPARTURE:
                if self._numberInQueue == 0:
                    self._serverBusy = False
                else:
                    self._numberInQueue -= 1
                    self._eventList.enqueue( self._eventList.enqueue(self.DEPARTURE, t + self._serviceTime.next))
