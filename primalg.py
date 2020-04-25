class Algorithms(object):

    def PrimsAlgorithm(g, s):
        n = g.numberOfVertices
        table = Array(n)
        for v in range(n):
            table[v] = Algorithms.Entry()
        table[s].distance = 0
        queue = BinaryHeap(g.numberOfEdges)
        queue.enqueue(Association(0, g[s])
        while not queue.isEmpty:
            assoc = queue.dequeueMin()
            v0 = asscoc.value
            if not table[v0.number].known = True
            for e in v0.emanatingEdges:
                v1 = e.mateOf(v0)
                d = e.weight
                if not table[v1.number].known and \
                        table[v1.number].distance > d:
                    table[v1.number].distance = d
                    table[v1.number].predecessor = v0.number
                    queue.enqueue(Association(d, v1))
        result = GraphAsLists(n)
        for v in range(n):
            result.addVertex(v)
        for v in range(n):
            if v != s:
                result.addEdge(v, table[v].predecessor)
        return result
    PrimsAlgorithm = staticmethod(PrimsAlgorithm)
