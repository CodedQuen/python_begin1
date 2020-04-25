class Tree(Container):

    class Iterator(Iterator):

        def __init__(self, tree):
            super(Tree.Iterator, self).__init__(tree)
            self._stack = StackAsLinkedList()
            if not tree.isEmpty:
                self._stack.push(tree)

        def next(self):
            if self._stack.isEmpty:
                raise StopIteration
            top = self._stack.pop()
            i = top.degree - 1
            while i >= 0:
                subtree = top.getSubtree(i)
                if not subtree.isEmpty:
                    self._stack.push(subtree)
                i -= 1
            return top.key

    def __iter__(self):
        return Tree.Iterator(self)
