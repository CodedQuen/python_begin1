class StraightSelectionSorter(Sorter):

    def __init__(self):
        super(StraightSelectionSorter, self).__init__()

    def _sort(self):
        i = self._n
        while i > 1:
            max = 0
            for j in range(i):
                if self._array[j] > self._array[max]:
                    max = j
            self.swap(i-1, max)
            i -= 1
