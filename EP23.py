# ການເຂົ້້າເຖິງໂຕອັກສອນໃນ String
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

name = 'ໄປຊືເຂົ້າ ແລະ ອາຫານຢູ່ຕະຫຼາດ'

x = 'ເຂົ້າ' not in name
if x:
    name = name.replace('ເຂົ້າ','ເປັດ')

print(name)
