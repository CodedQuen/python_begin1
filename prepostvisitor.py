class PrePostVisitor(Visitor):

    def __init__(self):
        super(PrePostVisitor, self).__init__()

    def preVisit(self, obj):
        pass

    def inVisit(self, obj):
        pass

    def postVisit(self, obj):
        pass

    visit = inVisit
