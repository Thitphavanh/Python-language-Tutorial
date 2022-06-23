# ຕາຕະລາງໝາກດາມ

number = int(input('ປ້ອນຂະໜາດ = '))  # 5 => 0,1,2,3,4

# 3 x 3
# row = 0 + column = 0
# row = 0 + 1
# row = 0 + 2

# row = 1 + column = 0
# row = 1 + 1
# row = 1 + 2

# row = 2 + column = 0
# row = 2 + 1
# row = 2 + 2

'''
xox
oxo
xox
'''

for row in range(number):
    for column in range(number):
        if (row + column) % 2 == 0:
            print('x', end='')
        else:
            print('o', end='')

    print(' ')

'''
for row in range(number):
    for column in range(number):
        print('X', end='') if (row + column) % 2 == 0  else print('O', end='')
    print(' ')
'''
