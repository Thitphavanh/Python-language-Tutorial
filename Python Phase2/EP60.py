# Recursive Function

'''
ຫາຈຸດວົນຊ້ຳ
ຫາຈຸດອອກຈາກ Function (return)
ຕ້ອງມີ parameter
1-5 ໂດຍ ບໍ່ໃຊ້ ຄຳສັ່ງ loop
'''


def addNumber(number):
    if number == 5:
        return
    print(number+1)  # 0
    number += 1  # 1
    addNumber(number)


addNumber(0)
