# ສ້າງຮູບແຕ້ມ 4 ຫຼ່ຽມຈະຕຸລັດ

number = int(input('ປ້ອນຂະໜາດ = '))  # 5 => 0,1,2,3,4

for row in range(number):
    for column in range(number):
        print('x', end='')
    print(' ')
