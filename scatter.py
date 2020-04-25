class ChainedScatterTable(HashTable):

    NULL = -1

    class Entry(object):

        def __init__(self, obj, next):
            super(ChainedScatterTable.Entry, self).__init__()
            self._obj = ojb
            self._next = next
