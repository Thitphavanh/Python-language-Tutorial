# break / continue

'''
i = 1
while i <= 10:
    print('ຮອບທີ =', i)
    if(i == 5):
        break
    i += 1
'''

'''
i = 1
while i < 10:
    i += 1
    if(i % 2 == 0):
        continue
    print('ຮອບທີ =', i)
'''

'''
for i in range(1, 11):
    if(i % 2 == 0):
        continue
    print(i)
'''

for i in range(1, 11):
    if(i == 5):
        break
    print(i)


print('ຈົບໂປຮແກຣມ')
