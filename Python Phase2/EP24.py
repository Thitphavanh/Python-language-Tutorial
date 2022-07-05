# ການຄົ້ນຫາ ແລະ ນັບຈຳນວນໂຕອັກສອນໃນສະມາຊິກ

messages = ['aa', 'aab', 'cba', 'bba', 'aba', 'cca', 'aaa', 'cab', 'aaaab']
result = []

for item in messages:
    result.append(item.count('a'))
print(result)
