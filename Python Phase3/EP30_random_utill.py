import random


for i in range(10):
    # r = random.random()  # 0.0 - 1.0
    # r = random.uniform(1, 99)  # 1 <= r < 99
    r = random.randrange(1, 99, 2)  # 1 <= r < 99
    print(r)
