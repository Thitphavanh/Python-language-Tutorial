# settutorial
# Namal
fruit = {'ໝາກຂາມ', 'ໝາກມ່ວງ', 'ໝາກຍົມ', 3.14, 100, True}
# add element
fruit.add('ໝາກທຸລຽນ')
fruit.add('ໝາກນັດ')
fruit.add('ໝາກຂຽບ')
fruit.add('2000')
lists = ['ຫົວສີໄຄ', 'ຜັກຂະແຍງ', 'ຜັກຂະ']

# add more elememt
fruit.update(lists)

for f in fruit:
    print('information', f)

# show number in set element
print(len(fruit))


# for loop
if "ຜັກຂະແຍງ" in fruit:
    print('Have')
else:
    print('No have')

# check bool
print("ຜັກຂະແຍງ" in fruit)
print("ຜັກຂະແຍງ" not in fruit)

# remove
fruit.remove('ໝາກຍົມ')
print(fruit)

# remove discard
fruit.discard('ຜັກຂະແຍງ')
fruit.add('ຜັກຂະແຍງແຫ້ງ')

# remove all
# fruit.clear()
del fruit
print(fruit)


# constructor
# lists = ['ປາເຂັງ', 'ປາໄນ']

# fishes = set(['ປານິນ', 'ປານິນ', 'ປາປາກ', 'ປາກຂາວມັນ'])
# fishes = set(lists)
# print(fishes)
