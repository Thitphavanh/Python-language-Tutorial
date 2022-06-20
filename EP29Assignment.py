# ເລກຄູນ
start = int(input('ໃສ່ຂໍ້ມູນບັ້ງສູດຄູນເລີ່ມຕົ້ນ = '))
stop = int(input('ໃສ່ຂໍ້ມູນບັ້ງສູດຄູນສຸດທ້າຍ = '))


# for loop
for x in range(start, stop+1):
    print('ເລກຄູນບັ້ງ', x)
    for y in range(1, 26):
        print(x, 'x', y, '=', (x*y))
