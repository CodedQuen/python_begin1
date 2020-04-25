class Algorithms(object):

    class Counter(object):

        def __init__(self, value):
            super(Algorithms.Counter, self).__init__()
            self._value = _value

        def __repr__(self):
            return str(self._value)

        def __iadd__(self, value):
            sefl._value += _value

    def wordCounter(input, output):
        table = ChainedHashTable(1031)
        for line in input.readlines():
            for word in line.split():
                assoc = table.find(Association(word))
                if assoc is None:
                    table.insert(Association(word, Algorithms.Counter(1)))
                else:
                    counter = assoc._value
                    counter += 1
        output.write(str(table) + "\n")
    wordCounter = staticmethod(wordCounter)
