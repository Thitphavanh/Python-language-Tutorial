# Check Charactor ຫາຈຳນວນຕົວອັກສອນພິມນ້ອຍ/ພິມໃຫຍ່


def CheckString(message):
    result = {'UPPER': 0, 'LOWER': 0}
    for c in message:
        if c.isupper():
            result['UPPER'] += 1
        elif c.islower():
            result['LOWER'] += 1
        else:
            pass
    return result


message = input('Input your message :')
x = CheckString(message)
print(x)
