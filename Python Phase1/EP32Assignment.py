sum = 0

'''
while sum != 100:
    number = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ :'))
    sum += number
    print('ຜົນລວມ =', sum)
'''

'''
while sum <= 100:
    number = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ :'))
    sum += number
    print('ຜົນລວມ =', sum)

'''


while True:
    number = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ :'))
    sum += number
    if sum>=100:
        break
    print('ຜົນລວມ =', sum)
