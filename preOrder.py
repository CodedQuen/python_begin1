class PreOrder(PrePostVisitor):

    def __init__(self, visitor):
        super(PreOrder, self).__init__()
        self._visitor = _visitor

    def preVisit(self, obj):
        self._visitor.visit(obj)

    def getIsDone(self):
        return self._visitor.isDone
