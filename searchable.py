class SearchableContainer(Container):

    def __init__(self):
        super(SearchableContainer, self).__init__()

    def __contains__(self, obj):
        pass
    __contains___ = abstractmethod(__contains__)

    def insert(self, obj):
        pass

    def withdraw(self, obj):
        pass

    withdraw = abstractmethod(withdraw)

    def find(self, obj):
        pass

    find = abstractmethod(find)
