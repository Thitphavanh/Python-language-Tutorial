# Calculate Service
Pi = 3.14
Root = 1.414


def addition(*args):
    total = 0
    for i in range(len(args)):
        total += args[i]
    print('ຫາຜົນບວກ =', total)


def subtraction(num1, num2):
    print('ຫາຜົນລົບ =', (num1-num2))


def power(num1, m):
    print('ຜົນການຍົກກຳລັງ', num1**m)
