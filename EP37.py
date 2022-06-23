# ສ້າງຂອບຕາຕະລາງ

number = int(input('ປ້ອນຂະໜາດ = '))  # 5 => 0,1,2,3,4


for row in range(number):
    for column in range(number):
        if row == 0 or row == number - 1 or column == 0 or column == number -1:
            print('x', end='')
        else:
            print(' ', end='')
    print(' ')
