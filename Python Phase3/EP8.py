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
        name = input('ກະລຸນາປ້ອນຊື່ຜຸ້ໃຊ້ງານ : ')
        if name == 'Joker':
            raise Exception('ບໍ່ສາມາດເຂົ້າລະບົບໃຊ້ງານໄດ້')

        number1 = int(input('ປ້ອນໂຕເລກ 1 : '))
        number2 = int(input('ປ້ອນໂຕເລກ 2 : '))
        if number1 == 0 and number2 == 0:
            break
        if number1 < 0 or number2 < 0:
            raise Exception('ບໍ່ສາມາດປ້ອນຄ່າຕິລົບໄດ້')

        result = number1/number2
        print(result)

    except Exception as e:
        print(e)

    finally:
        print('ເຮັດວຽກຕໍ່ໄປ......')
