# ໂປຣແມຣມຄຳນວນ BMI


weight = int(input('ປ້ອນນ້ຳໜັກຂອງເຈົ້າ (kg) : '))
high = int(input('ປ້ອນນ້ຳໜັກຂອງເຈົ້າ (cm) : '))/100

bmi = weight/(high**2)


if bmi >= 0 and bmi < 18.0:
    result = 'ຈ່ອຍ'
elif bmi >= 18.5 and bmi <= 22.9:
    result = 'ສົມສ່ວນ'
elif bmi >= 23.0 and bmi <= 24.9:
    result = 'ນ້ຳໜັກເກີນ'
elif bmi >= 25.0 and bmi <= 29.9:
    result = 'ໂລກອ້ວນ ລະດັບ 1'
elif bmi > 30:
    result = 'ໂລກອ້ວນ ລະດັບ ອັນຕະລາຍ'
else:
    result = 'ບໍ່ຮູ້ຄ່າທີ່ຊັດເຈນ'
print('ຄ່າ bmi = ', bmi, 'ຄາດການ = ', result)
