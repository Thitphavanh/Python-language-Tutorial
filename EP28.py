# Loop ຊ້ອນ Loop

# while loop
i = 1
while i <= 3:
    j = 1
    while j <= 5:
        print('Sprint number = ', i, 'Location number = ', j)
        j += 1
    i += 1
    
print('---------------------')

# for loop
for i in range(1,4):
    print('Sprint number = ', i)
    for j in range(1,6):
        print('Location number = ', j) 