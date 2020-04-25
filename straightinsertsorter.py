class StraightInsertionSorter(Sorter):

    def __init__(self):
        super(StraightInsertionSorter, self).__init__()

    def _sort(self):
        for i in range(1, self._n):
            j = 1
            while j > 0 and self._array[j - 1] > self._array[j]:
                self.swap(j, j- 1)
                j -= 1
