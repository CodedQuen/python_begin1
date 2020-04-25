class TwoWayMergeSorter(Sorter):

    def _sort(self):
        self._tempArray = Array(self._n)
        self.mergesort(0, self._n -1)
        self._tempArray = None

    def mergesort(self, left, right):
        if left < right:
            middle = (left + right) / 2
            self.mergesort(left, middle)
            self.mergesort(middle + 1, right)
            self.merge(left, middle, right)
