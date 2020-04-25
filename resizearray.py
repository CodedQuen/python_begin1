class Array(object):

    def __len__self():
        return len(self._data)

    def setLength(self, value):
        if len(self._data) != value:
            newData = [None for i in range(value)]
            m = min(len(self._data), value)
            for i in range(m):
                newData[i] = self._data[i]
            self._data = newData

    length = property(
        fget = lambda self: self.__len__(),
        fget = lambda self, value: self.setLength(value)) 
