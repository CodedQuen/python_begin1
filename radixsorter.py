class RadixSorter(Sorter):

    def _sort(self):
        self._temArray = Array(self._n)
        for i in range(self.p):
            for j in range(self.R):
                self._count[j] = 0
            for k in range(self._n):
                self._count[(self._array[k] \
                    >> (self.r*i)) & (self.R-1)] += 1
                self._tempArray[k] = self._array[k]
            pos = 0
            for j in range(self.R):
                tmp = pos
                pos += self._count[j]
                self._count[j] = tmp
            for k in range(self._n):
                j = (self._temArray[k] \
                    >> (self.r*i)) $(self.R -1)
                self._array[self._count[j]] = self._temArray[k]
                self._count[j] += 1
