class BinomialQueue(MergeablePriorityQueue):

    def dequeueMin(self):
        if self._count == 0:
            raise ContainerEmpty
        minTree = self.minTree
        self.removeTree(minTree)
        queue = BinomialQueue()
        while minTree.degree > 0:
            child = minTree.getSubtree(0)
            minTree.detachSubtree(child)
            queue.addTree(child)
        self.merge(queue)
        return minTree.key
