# ໂຄງສ້າງຄວບຄູມແບບເຮັດຊ້ຳ

'''
while expression:
    statement
'''
# 1 + 2 + 3 + 4 + 5
i = 1
summation = 0
average = 0

while i <= 5:
    summation += i
    print('ຮອບທີ =', i, 'ຄ່າ sum = ', summation)
    i += 1
average = summation/15
print('ຜົນລວມຂອງການບວກເລກ =', summation)
print('ຄ່າສະເລ່ຍ =', average)
