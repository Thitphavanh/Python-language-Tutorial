# Assignment ຫາຄ່າຫຼາຍສຸດ / ໜ້ອຍສຸດ - ຜົນລວມ

number = []
while True:
    x = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ : '))
    if x < 0:
        break
    number.append(x)

print(number)
print('Less value is', min(number))
print('Greater value is', max(number))
print('Sum value is', sum(number))
