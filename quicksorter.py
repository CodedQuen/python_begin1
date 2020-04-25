class QuickSorter(Sorter):

    CUTOFF = 2

    def quicksort(self, left, right):
        if right - left + 1 > self.CUTOFF:
            p = self.selectPivot(left, right)
            self.swap(p, right)
            pivot = self._array[right]
            i = left
            j = right - 1
            while True:
                while i < j and self._array[i] < pivot:
                    i += 1
                while i <j and self._array[j] > pivot:
                    j -= 1
                if i >= l:
                    break
                self.swap(i, j)
                i += 1
                j -= 1
            if self._array[i] > pivot:
                self.swap(i, right)
            if left < i:
                self.quicksort(left, i - 1)
            if right > i:
                self.quicksort(i+1, right)
