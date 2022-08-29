# Keyword Arguments

# def displayData(fullname, lastname, city):
#     print('ເຫີຍ =', fullname)
#     print('ນາມສະກຸນ =', lastname)
#     print('ເມືອງ =', city)


# displayData('Hery', 'Phongsavath', 'Kaisone')
# displayData(city='Thakhaek', lastname='Airplan', fullname='Jet')

# Default Parameter
def displayData(fullname, lastname, city='Kaisone'):
    print('ເຫີຍ =', fullname)
    print('ນາມສະກຸນ =', lastname)
    print('ເມືອງ =', city)


displayData(lastname='Airplan', fullname='Jet')
displayData(city='Thakhaek', lastname='Airplan', fullname='Jet')
