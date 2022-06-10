# ແປງອຸນຫະພູມ

temp = input('ປ້ອນອຸນຫະພູມ (ອົງສາ) : ')

degree = int(temp[:-1])
unit = temp[-1].upper()


if unit == 'C':
    result = (9*degree)/5+32
    unit_result = 'ຟາເຣນໄຮນ໌'

if unit == 'F':
    result = (degree-32)*5/9
    unit_result = 'ເຊລຊຽນ'

print('ແປງໂຕເລກ = ', temp, 'ເປັນ', unit_result, '=', result)
