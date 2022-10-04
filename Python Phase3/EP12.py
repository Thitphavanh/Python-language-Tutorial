try:
    read_file = open('score.txt', 'r', encoding='utf-8')
    line = read_file.readlines()
    for x in line:
        print(x)
    read_file.close()
except FileNotFoundError:
    print('ຫາ File ບໍ່ເຫັນ')
