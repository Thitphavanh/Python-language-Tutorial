# ຈັບຄູ່ຄຳທັກທາຍ / ບຸກຄົນ

greeting = ['ສະບາຍດີ', 'Hi', 'Hello', 'Good bye']
people = ['Jo', 'James', 'Noy']
result = []

# ແບບປົກກະຕິ
for x in greeting:
    for y in people:
        result.append(x+y)
# print(result)

# ແບບຫຼຸດຮູບ
result = [x+y for x in greeting for y in people]
print(result)
