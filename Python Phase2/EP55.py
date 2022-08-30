# function return ຄ່າ

"""
1. ບໍ່ມີການຮັບຄ່າ ແລະ ສົ່ງຄ່າ
def name():

2. ມີການຮັບຄ່າເຂົ້າໄປເຮັດວຽກ
def name(a,b):

3. ຮັບຄ່າເຂົ້າໄປເຮັດວຽກ ແລະ ສົ່ງອອກມາ
def name(a,b):
    return a+b
    
4.ບໍ່ມີການຮັບຄ່າເຂົ້າມາ ແຕ່ສົ່ງຄ່າອອກໄປ
"""


def add(a, b):
    return a+b


x = add(10, 20)
print(x)


def showNumber():
    return 500


# x = showNumber()
# print('ໂຕເລກ =', x)

print(showNumber())


def randomNumber(x):
    if x == '100':
        print('ຖືກເລກ')
        return 10000000
    else:
        print('ບໍ່ຖືກ, ແມ່ແດກ')
        return 0


money = randomNumber('520')
owe = 1500000
result = money-owe
print('ເງິນລາງວັນ =', money)
print('ເງິນຍັງເຫຼືອ =', result)
