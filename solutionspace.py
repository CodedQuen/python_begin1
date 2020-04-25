class Solution(Object):

    def __init__(self):
        super(Solution, self).__init__()

    def getIsFeasible(self):
        pass
    getIsFeasible = abstractmethod(getIsFeasible)

    IsFeasible = property(
        fget = lambda self: self.getIsFeasible())

    def getIsComplete(self):
        pass
    getIsComplete = abstractmethod(getIsComplete)

    isComplete = property(
        fget = lambda self: self.getIsComplete())

    def getObjective(self):
        pass
    getObjective = abstractmethod(getObjective)

    objective = property(
        fget = lambda self: self.getObjective())

    def getBound(self):
        pass
    getBound = abstractmethod(getBound)

    bound = property(
        fget = lambda self: self.getBound())

    def getSuccessors(self):
        pass
    getSuccessors = abstractmethod(getSuccessors)

    successors = property(
        fget = lambda self: self.getSuccessors()0
