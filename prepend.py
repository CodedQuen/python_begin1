class LinkedList(object):

    def prepend(self, item):
        tmp = self.Element(self, item, self._head)
        if self._head is None:
            self._tail = tmp
        self._head = tmp 
