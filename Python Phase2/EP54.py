# List Parameter

def displayCarsList(items):
    for i in range(len(items)):
        print('ລົດຄັນທີ ', i+1, '=', items[i])


cars = ['Bugetti', 'Ferrari']
displayCarsList(cars)


def displayEVCarsTuple(items):
    for i in range(len(items)):
        print('ລົດໄຟຟ້າຄັນທີ ', i+1, '=', items[i])


evcars = ['Tesla', 'Lucid Air', 'BYD']
displayEVCarsTuple(evcars)
