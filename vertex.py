class Vertex(Object):

    def __init__(self):
        super(Vertex, self).__init__()

    def getNumber(self): pass
    getNumber = abstractmethod(getNumber)
    number = property(
        fget = lambda self: self.getNumber())

    def getWeight(self): pass
    getWeight = abstractmethod(getWeight)
    weight = property(
        fget = lambda self: self.getWeight())

    def getIncidentEdges(self): pass
    getIncidentEdges = abstractmethod(getIncidentEdges)
    getIncidentEdges = property(
        fget = lambda self: self.getIncidentEdges())

    def getEmanatingEdges(self): pass
    getEmanatingEdges = abstractmethod(getEmanatingEdges)
    emanatingEdges = property(
        fget = lambda self: self.getEmanatingEdges())

    def getPredecessors(self): pass
    getPredecessors = abstractmethod(getPredecessors))
    predecessors = property(
        fget = lambda self:self.getPredecessors())

    def getSuccessors(self): pass
    getSuccessors = abstractmethod(getSuccessors)
    successors = property(
        fget = lambda self: self.getSuccessors())
