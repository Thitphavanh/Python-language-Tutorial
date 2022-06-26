from audioop import avg


start, stop = 1, 5

sum = 0
agv = 0
while(start <= stop):
    number = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ :'))
    sum += number
    start += 1

avg = sum/stop
print('ຜົນລວມ =', sum)
print('ຄ່າສະເລ່ຍ =', avg)
