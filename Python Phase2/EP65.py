# Find Number Phone ຄົ້ນຫາເບີໂທລະສັບ
data = {'191': 'ແຈ້ງເຫດດ່ວນ', '101': 'ລົດໂຮງໝໍ', '189': 'ລົດດັບເພີງ'}


def searchNumber(message):
    for key, value in data.items():
        if value == message:
            print('ເບີຕິດຕໍ່ : ', key)
        # else:
        #     print('ບໍ່ມີຂໍ້ມູນ')
        #     return


message = input('ປ້ອນຂໍ້ມູນທີ່ຕ້ອງການ : ')
searchNumber(message)
