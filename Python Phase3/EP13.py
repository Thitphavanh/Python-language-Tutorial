try:
    read_file = open('score.txt', 'r', encoding='utf-8')
    line = read_file.readlines()
    for x in line:
        print(x)

    write_file = open('score.txt', 'a', encoding='utf-8')
    write_file.writelines('ສະບາຍດີທຸກຄົນ')

    read_file.close()
    write_file.close()

except FileNotFoundError:
    print('ຫາ File ບໍ່ເຫັນ')
