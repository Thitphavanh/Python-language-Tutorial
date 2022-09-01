# **kwargs

# *args => ຄ່າໃນ parameter ມີໄດ້ຫຼາຍຄ່າ
def add(*number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    print(sum)

# ຊື່ parameter ມີຫຼາຍຊື່


def displayData(**kwargs):
    print(kwargs)


displayData(full_name='Beer', last_name='China', age=27)
displayData(full_name='Beer', last_name='Laos', age=28)
displayData(full_name='Beer', last_name='Thailand', age=30, status='single')
displayData(status='rich')
displayData(full_name='Beer', last_name='Thailand', city='Kaisone', status='single')

# ຊື່ parameter ມີຫຼາຍຊື່
# Show only full_name
# def displayData(**item):
#     print(item)


# displayData(full_name='Beer', last_name='China', age=27)
# displayData(full_name='Beer', last_name='Laos', age=28)
# displayData(full_name='Beer', last_name='Thailand', age=30, status='single')
# displayData(status='rich')
# displayData(full_name='Beer', last_name='Thailand', city='Kaisone', status='single')
