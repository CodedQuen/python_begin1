class Stack(Container):

    def __init__(self):
        super(Stack, self).__init__()

    def getTop(self):
        pass
    getTop = abstractmethod(getTop)

    top = property(
        fget = lambda self: self.getTop())

    def push(self, obj):
        pass
    push = abstractmethod(push)

    def pop(self):
        pass
    pop = abstractmethod(pop)
