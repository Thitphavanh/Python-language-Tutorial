# Fibonacci Number

# 0, 1, 1, 2, 3, 5, 8, 13, 21......
# f0 = ?, f1 = ?
def fibonacci(number):
    if number <= 1:  # ເລກ 2 ລຳດັບທຳອິດ
        return number

    else:  # ເລກລຳດັບຖັດໄປ
        return fibonacci(number-1) + fibonacci(number-2)


for i in range(5):  # 0 - 4
    print(fibonacci(i))  # 0, 1, 1, 2, 3
