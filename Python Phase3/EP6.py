# Exception
'''
try:
    ຄຳສັ່ງງຣັນໂປຣແກຣມປົກກະຕິ
except:
    ຄຳສັ່ງທີ່ເຮັດວຽກຕອນໂປຣແກຣມມີຂໍ້ຜິດພາດ  
    
ValueError -> ຄ່າຜິດພາດ 
ZeroDivisionError
'''

try:
    number1 = int(input('ປ້ອນໂຕເລກ 1 : '))
    number2 = int(input('ປ້ອນໂຕເລກ 2 : '))
    result = number1/number2
    print(result)

except Exception as e:
    print(e)

finally:
    print('ເຮັດວຽກຕໍ່ໄປ......')
