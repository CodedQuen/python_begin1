class Queue(Container):

    def __init__(self):
        super(Queue, self).__init__()

    def getHead(self):
        pass
    getHead = abstractmethod(getHead)

    head = property(
        fget = lambda self: self.getHead())

    def enqueue(self, obj):
        pass
    enqueue = abstractmethod(enqueue)

    def dequeue(self):
        pass
    dequeue = abstractmethod(dequeue)
