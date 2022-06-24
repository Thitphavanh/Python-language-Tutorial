# ເກມທວາຍເລກລູກເຕົາ
import random

myrandom = random.randrange(1, 11)
k = 1
correct = False
print('ເຈົ້້າມີໂອກາດຕອບ 3 ເທື່ອ \n')

while True:
    number = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ = '))
    correct = (number == myrandom)

    if not correct:
        if(number > myrandom):
            print('ນ້ອຍກວ່າ')
        if(number < myrandom):
            print('ຫຼາຍກວ່າ')

    if correct:
        print('ຕອບຖືກຮັບໄປເລີຍລົດ Tesla Model Y 1 ຄັນ')
        break

    if number < 0 or k == 3:
        break
    k += 1
    
if not correct:
    print('ເສຍໃຈນຳ ເຈົ້າຕອບບໍ່ຖືກ')
    print('ສະເລີຍ =', myrandom)
