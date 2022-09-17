# Recursive Function

'''
ຫາຈຸດວົນຊ້ຳ
ຫາຈຸດອອກຈາກ Function (return)
ຕ້ອງມີ parameter
1-5 ໂດຍ ບໍ່ໃຊ້ ຄຳສັ່ງ loop
'''


from re import X


def addNumber(number):
    if number == 5:
        return
    print(number+1)  # 0
    number += 1  # 1
    addNumber(number)


def summation(number):
    if number == 1:
        return number
    else:
        return number + summation(number-1)


x = summation(5)  # ? = 5+4+3+2+1
print(x)

''''
5
5 + summation(4)
5 + 4 + summation(3)
5 + 4 + 3 + 2 + summation(2)
5 + 4 + 3 + 2 + 1 + summation(1)
5 + 4 + 3 + 2 + 1
'''
