
tups = (100, 251, 315, 412, 145, 3.14, 4)
print('Before :',tups)
lists = list(tups)
lists.sort()
lists.reverse()
tups = tuple(lists)
print('After :',tups)



