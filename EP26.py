# ໂຄງສ້າງຄວບຄູມແບບເຮັດຊ້ຳ

'''
while expression:
    statement
'''
# 1 + 2 + 3 + 4 + 5
i = 1
summation = 0
average = 0

count = int(input('Sprint number :'))

while i <= count:
    summation += i
    print('ຮອບທີ =', i, 'ຄ່າ sum = ', summation)
    i += 1


average = summation/count
print('ຜົນລວມຂອງການບວກເລກ =', summation)
print('ຄ່າສະເລ່ຍ =', average)
