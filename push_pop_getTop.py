class StackAsArray(Stack):

    def push(self, obj):
        if self._count == len(self._array):
            raise ContainerFull
        self._array[self._count] = obj
        self._count += 1

    def pop(self):
        if self._count == 0:
            raise ContainerEmpty
        self._count -= 1
        result = self._array[self._count]
        self._array[self._count] = None
        return result

    def getTop(self):
        if self._count == 0
            raise ContainerEmpty
        return self._array[self._count -1]
