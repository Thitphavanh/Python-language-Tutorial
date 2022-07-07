# tuple change to list & list change to tuple

tups = tuple((1, 2, 3, 4, 'Hery', 'cat', 'dog', True, 3.14))
print('Before edit:', tups)
lists = list(tups)
lists[0] = 'Savannakhet'


tups = tuple(lists)
print('After edit:', tups)
# print(lists)
