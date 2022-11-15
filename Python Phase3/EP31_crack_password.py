# Crack Password
import random


ATM_Password = 'hery23'
result = ""  # ສຳລັບເກັບຜົນລັບ


while result != ATM_Password:
    result = ""
    for letter in range(len(ATM_Password)):
        list_number = random.choice('0123456789abcdefghijklmnprstuvwxyz')
        result = "".join(list_number)+str(result)
        print("Search =", result)
print("Crack Password is ", result)
