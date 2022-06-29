# Assignment ຮັບແລະລຽງລຳດັບຂໍ້ມູນຕົວເລກ

number = []
while True:
    x = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ : '))
    if x < 0:
        break
    number.append(x)

print('Before ->', number)
number.sort()
print('Less to greater ->', number)
number.reverse()
print('Greater to less ->', number)
print('End program')
