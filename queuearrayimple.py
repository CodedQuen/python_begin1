class QueueAsArray(Queue):

    def __init__(self, size = 0):
        super(QueueAsArray, self).__init__()
        self._array = Array(size)
        self._head = 0
        self._tail = size -1

    def purge(self):
        while self._count > 0:
            self._arrayp[self._head] = None
            self._head = self._head + 1
            if self._head == len(self._array):
                self._head = 0
            self._count -= 1
