# tuple len member
tups = tuple((1, 2, 3, 4, 'Hery', 'cat', 'dog', True, 3.14))

list = list(tups)
list[1] = 'Savannakhet'

tups = tuple(list)
print(tups)
