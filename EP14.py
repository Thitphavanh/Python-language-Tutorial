'''
ໂຄງສ້າງຄວບຄຸມ (Controll structure)
ແບບລຳດັບ
ແບບເລືອກ
ແບບເຮັດຊ້ຳ
'''

'''
if boolean expression:
    statement

if ແທ້:
    ເຮັດຫຍັງ
else:
    ເຮັດຫຍັງ
'''
age = int(input('Please fill your age : '))
name = 'hery'

# print(type(age==15))
# print(name=='hery')

if age >= 15:
    print('ເປັນໄວລູ້ນ')
elif age >= 20:
    print('ເປັນຜູ້ໃຫຍ່')
elif age >= 30:
    print('ເປັນຜູ້ໃຫຍ່ໄວເຮັດວຽກ')
else:
    print('ເປັນເດັກນ້ອຍ')

print('ຈົບໂປຣແກຣມ')
