# Assignment ຫາເລກຄູ່ / ເລກຄີກ 
number = []

# ເລກຄີກ
odd = []
# ເລກຄູ່
even = []

while True:
    x = int(input('ປ້ອນໂຕເລກຂອງເຈົ້າ : '))
    if x < 0:
        break
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
    number.append(x)

print('Total number ->', number)
print('ເລກຄີກ ->', odd)
print('ເລກຄູ່ ->', even)
