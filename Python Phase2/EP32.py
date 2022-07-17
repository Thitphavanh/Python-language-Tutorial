# tuple len member
tups = (1, 2, 3, 4, 'Hery', 'cat', 'dog', True, 3.14)
print('Before :', tups)
lists = list(tups)
lists.remove(1)
tuple(lists)
tups = tuple(lists)
print('After :', tups)
