#!/usr/bin/python3
class VerboseList(list):
    def append(self, x):
        super().append(x)
        print('Added {} to the list.'.format(x))

    def extend(self, x):
        super().extend(x)
        print('Extended the list with {} items.'.format(len(x)))

    def remove(self, x):
        super().remove(x)
        print('Removed {} from the list.'.format(x))

    def pop(self, x=-1):
        print('Popped {} from the list.'.format(self[x]))
        deleted = super().pop(x)
        return deleted


lst = VerboseList()
lst.append('a')
lst.extend(['b', 'c', 'd'])
lst.remove('b')
lst.pop(1)