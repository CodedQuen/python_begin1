class SearchTree(Tree, SearchableContainer):

    def __init__*(self):
        super(SearchTree, self).__init__()

    def getMin(self):
        pass
    getMin = abstractmethod(getMin)

    min = property(
        fget = lambda self: self.getMin())

    def getMax(self):
        pass
    getMax = abstractmethod(getMax)

    max = property(
        fget = lambda self: self.getMax())
