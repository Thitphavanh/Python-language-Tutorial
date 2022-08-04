# set operator

fruitA = {'ໝາກຂາມ', 'ໝາກມ່ວງ', 'ໝາກຍົມ', 'ໝາກໂມ', 'ໝາກທູລຽນ', 'ໝາກນັດ'}
fruitB = {'ສຕອວ໌ເບອຣຣີ່', 'ກີວີ', 'ແອປເປິ້ລ', 'ໝາກທູລຽນ', 'ໝາກນັດ'}

# union
allfruit = fruitA.union(fruitB)
print(allfruit)

# update
fruitA.update(fruitB)
print(fruitA)

# copy
fruitC = fruitA.copy()
print(fruitC)

# difference
fruitC = fruitB.difference(fruitA)
print(fruitC)

# intersection
fruitC = fruitA.intersection(fruitB)
print(fruitC)

# difference_update
fruitA.difference_update(fruitB)
print(fruitA)

# intersection_update
fruitA.intersection_update(fruitB)
print(fruitA)


# subset
fishes = {'ປາດຸກ', 'ປານິນ', 'ປາຄໍ່', ' ປາປາກ', 'ປາຂາວມັນ', ' ປາເພ້ຍ'}


fishes_x = {'ປາປາກ', 'ປາຂາວມັນ'}
fishes_y = {'ປາມຶກ', 'ປາສະລາມ'}

print(fishes_x.issubset(fishes))
print(fishes.issuperset(fishes_x))
print(fishes.issuperset(fishes_y))
