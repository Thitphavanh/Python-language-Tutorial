# ໂປຣແກຣມຄຳນວນຄ່າ (ດັດສະນີມວນກາຍ)
# BMI = ນ້ຳໜັກ (Kg) / ສ່ວນສູງ * ສ່ວນສູງ (m)

weight = int(input('ປ້ອນນ້ຳໜັກຂອງເຈົ້າ (Kg) : '))
high = int(input('ປ້ອນສ່ວນສູງຂອງເຈົ້າ (Cm) : '))

# process
# cm => m
high /= 100

# caculate bmi
bmi = weight / (high**2)

# output
print('BMI = ', bmi)
