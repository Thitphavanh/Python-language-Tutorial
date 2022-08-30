# function return ຄ່າ

def randomNumber(x):
    if len(x) < 3:
        return
    if x == '100':
        print('ຖືກເລກ')
        return 10000000
    else:
        print('ບໍ່ຖືກ, ແມ່ແດກ')
        return 0


money = randomNumber('150')
print('ເງິນລາງວັນ =', money)
