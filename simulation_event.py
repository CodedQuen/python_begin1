class Simulation(object):

    class Event(Association):

        def __init__(self, type, time):
            super(Simulation.Event, self).__init__(time, type)

        time = property(
            fget = lambda self: self.getKey())

        type = property(
            fget = lambda self: self.getValue())
