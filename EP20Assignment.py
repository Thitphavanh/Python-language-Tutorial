# ແລກເງິນ ແລະ ຫາຈຳນວນເງິນໄດ້ເທົ່າໃດໃບ

# 150000 => 100000 => 1 ໃບ, 50000 => 1 ໃບ
# 80000 => 50000 => 1 ໃບ, 20000 => 1 ໃບ, 10000 => 1 ໃບ
# 25000 => 20000 => 1 ໃບ, 5000 => 1 ໃບ

number = int(input('Please fill your money : '))


# 350000
if number >= 100000:
    print('100000 ກີບ =', number//100000, 'ໃບ')
    number %= 100000

if number >= 50000:
    print('50000 ກີບ =', number//50000, 'ໃບ')
    number %= 50000

if number >= 20000:
    print('20000 ກີບ =', number//20000, 'ໃບ')
    number %= 20000

if number >= 10000:
    print('10000 ກີບ =', number//10000, 'ໃບ')
    number %= 10000

if number >= 5000:
    print('5000 ກີບ =', number//5000, 'ໃບ')
    number %= 5000

if number >= 2000:
    print('2000 ກີບ =', number//2000, 'ໃບ')
    number %= 2000


if number >= 1000:
    print('1000 ກີບ =', number//1000, 'ໃບ')
    number %= 1000


if number >= 500:
    print('500 ກີບ =', number//500, 'ໃບ')
    number %= 500
