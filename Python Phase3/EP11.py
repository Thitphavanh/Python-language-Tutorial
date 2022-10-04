try:
    write_file = open('score.txt', 'a', encoding='utf-8')
    for i in range(2):
        name = input('ປ້ອນຂໍ້ຄວາມທີ່ຕ້ອງການ : ')
        write_file.writelines(name+'\n')
    write_file.close()
except FileNotFoundError:
    print('ຫາ File ບໍ່ເຫັນ')
