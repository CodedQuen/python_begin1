class BinaryTree(Tree):

    def getLeft(self):
        if self.isEmpty:
            raise StateError
        return self._left

    left = property(
        fget = lambda self: self.getLeft())

    def getRight(self):
        if self.isEmpty:
            raise StateError
        return self._right

    right = property(
        fget = lambda self: self.getRight())
