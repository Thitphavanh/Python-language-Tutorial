# ຄົ້ນຫາໂຕເລກ ນ້ອຍສຸດ / ຫຼາຍສຸດ
max = 0
min = 9999


while True:
    number = int(input('ປ້ອນໂຕເລກ : '))
    if number < 0:
        break
    if number > max:
        max = number
    if number < min:
        min = number

print('ຄ່າຕ່ຳສຸດ :',min)
print('ຄ່າສູງສຸດ :',max)
