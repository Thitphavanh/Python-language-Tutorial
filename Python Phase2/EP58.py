# Function ເອີ້ນ Function

def equal(x, y, z):
    a = compareMax(x, y)
    m = compareMax(a, z)
    return m


def compareMax(x, y):
    if x > y:
        return x
    else:
        return y


# max = compareMax(10, 20)
# print('ຄ່າຫຼາຍທີ່ສຸດ =', max)


max = equal(10, 20, 30)
print('ຄ່າຫຼາຍທີ່ສຸດ =', max)
