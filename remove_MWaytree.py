class MWayTree(SearchTree):

    def withdraw(self, obj):
        if self.isEmpty:
            raise KeyError
        index = self.findIndex(obj)
        if index != 0 and self._key[index] == obj:
            if not self._subtree[index - 1].is Empty:
                max = self._subtree[index -1].max
                self._key[index] = max
                self._subtree[index - 1].withdraw(max)
            elif not self._subtree[index].isEmpty:
                min = self._subtree[index].min
                self._key[index] = min
                self._subtree[index].withdraw(min)
            else:
                self._count = self._count - 1
                i = index
                while i <= self._count:
                    self._key[i] = self._key[i+1]
                    self._subtree[i] = self._subtree[i+1]
                    i = i + 1
                self._keyp[i] = None
                self._subtree[i] = None
                if self._count == 0:
                    self._subtree[0] = None
        else:
            self._subtree(index).withdraw(obj)
