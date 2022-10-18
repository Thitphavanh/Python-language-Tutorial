import os

try:
    if os.path.exists('score.txt'):
        os.remove('score.txt')
        print('ໄດ້ລົບ File ແລ້ວ')
    else:
        print('ຫາ File ບໍ່ເຫັນ')
except Exception as e:
    print(e)
