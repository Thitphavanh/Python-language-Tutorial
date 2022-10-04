try:
    read_file = open('score.txt', 'r', encoding='utf-8')
    print(read_file.read())
except FileNotFoundError:
    print('ຫາ File ບໍ່ເຫັນ')
