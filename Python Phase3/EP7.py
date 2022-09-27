# Exception
'''
try:
    ຄຳສັ່ງງຣັນໂປຣແກຣມປົກກະຕິ
except:
    ຄຳສັ່ງທີ່ເຮັດວຽກຕອນໂປຣແກຣມມີຂໍ້ຜິດພາດ  
    
ValueError -> ຄ່າຜິດພາດ 
ZeroDivisionError
'''
while True:
    try:
        number1 = int(input('ປ້ອນໂຕເລກ 1 : '))
        number2 = int(input('ປ້ອນໂຕເລກ 2 : '))
        if number1 == 0 and number2 == 0:
            break
        result = number1/number2
        print(result)

    except ValueError:
        print('ກະລຸນາປ້ອນໂຕເລກ')

    except ZeroDivisionError:
        print('ຫ້າມຫານດ້ວຍເລກສູນ')

    finally:
        print('ເຮັດວຽກຕໍ່ໄປ......')
