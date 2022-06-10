# 1 ການເຂົ້້າເຖິງໂຕອັກສອນໃນ String
# 2 len function
# 3 ລຶບຊ່ຶງຊ້າຍຂວາ (strip)
# 4 ແປງ case ຂອງ string
# 5 ການແທນທີ່
# 6 ການກວດສອບຂໍ້ຄວາມ => True, False
# 7 ການຕໍ່ String (Concatinate) +
# 8 ການຈັດຮູບແບບການສະແດງຜົນ {}
# 9 ນັບຈຳນວນຄຳໃນປະໂຫຍກ
# ກວດສອບຄຳຂຶ້ນຕົ້ນ / ກວດສອບຄຳລົງທ້າຍ

# name = '  hery phenomenal : 27  '

# # ນັບ index
# print(len(name))
# print('ອາຍຸ = ', name[-2:])

# # ລົບຊ່ອງວ່າງ
# name = name.strip()
# print(len(name))

# # ລົບຊ່ອງວ່າງທາງຊ້າຍ
# name = name.lstrip()
# print(len(name))


# # ລົບຊ່ອງວ່າງທາງຂວາ
# name = name.rstrip()
# print(len(name))

# # index => 0
# name = 'hery ຮຽນຢູ່ປີ 4 ໄດ້ເກດ 4 ຢູ່ຊອຍ 4'

# # print(name.capitalize())
# print(name.replace('4','3.5',1))

# 7
# name = 'ໄປຊືເຂົ້າ ແລະ ອາຫານຢູ່ຕະຫຼາດ'

# x = 'ເຂົ້າ' not in name
# if x:
#     name = name.replace('ເຂົ້າ','ເປັດ')

# print(name)


# 8
# fnam = 'Hery'
# lname = 'Phongsavath'
# age = '24'
# employment = 'Programmer'
# salary = 1500000.124545

# text = ('ຊື່ຂຶ້ນຕົ້ນ : {}, ນາມສະກຸນ : {}, ອາຍຸ : {}, ອາຊີບ {}, ເງິນເດືອນ {:,.2f}')

# print(text.format(fnam, lname, age, employment, salary))

# 9
# market = 'I went to the market, buy some milk, bread and after to meet friends'

# print(market.count('went'))


# 10
# name = 'Mrs. Nang'

# # print(name.startswith('Mr.'))
# if name.startswith('Mr.'):
#     print('Men')
# else:
#     print('Women')

name = '7788'

if name.endswith('8'):
    print('Lucky number')
else:
    print('not good')