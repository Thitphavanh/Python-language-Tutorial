# Bank Accounting

# data
accounts = {'Robert': 5000000, 'Anne': 80000000}


def getBalance():
    print('ຍອດເງິນຄົງເຫຼືອໃນບັນຊີ :', accounts)


def deposite(money):
    if not type(money) is int and not type(money) is float:
        raise Exception('ການຝາກເງິນຕ້ອງເປັນຈຳນວນໂຕເລກເທົ່ານັ້ນ')
    if money <= 0:
        raise Exception('ຈຳນວນໂຕເລກຕ້ອງເປັນບວກເທົ່ານັ້ນ')
    print('ຝາກເງິນເຂົ້າບັນຊີ Robert :', money)
    accounts['Robert'] += money


def withdraw(money):
    if not type(money) is int:
        raise Exception('ການຖອນເງິນຕ້ອງເປັນຈຳນວນໂຕເລກເທົ່ານັ້ນ')
    if money <= 50000:
        raise Exception('ບໍ່ສາມາດຖອນເງິນໄດ້ ລະບົບໄດ້ກຳນົດໃຫ້ມີຍອດຄົງເຫຼືອໃນບັນຊີ ເປັນຈຳນວນເງິນ 50000')
    if money > accounts['Robert']:
        raise Exception('ຈຳນວນເງິນໃນບັນຊີບໍ່ພຽງພໍ')
    print('ຖອນເງິນອອກຈາກບັນຊີ Robert :', money)
    accounts['Robert'] -= money


def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception('ການໂອນເງິນຕ້ອງເປັນຈຳນວນໂຕເລກເທົ່ານັ້ນ')
    if money <= 0:
        raise Exception('ຈຳນວນໂຕເລກຕ້ອງເປັນບວກເທົ່ານັ້ນ')
    if money > accounts['Robert']:
        raise Exception('ຈຳນວນເງິນໃນບັນຊີບໍ່ພຽງພໍ')
    print('ໂອນເງິນໄປຫາບັນຊີ Anne :', money)
    accounts['Anne'] += money
    accounts['Robert'] -= money


try:
    getBalance()
    withdraw(490000)
    getBalance()
except Exception as e:
    print(e)
