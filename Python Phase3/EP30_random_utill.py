import random


items = [1, 2, 5, 6, 7, 8, 9, 10, 'C', 'D']

for i in range(15):
    # r = random.random()  # 0.0 - 1.0
    # r = random.uniform(1, 99)  # 1 <= r < 99
    # r = random.randrange(1, 99, 2)  # 1 <= r < 99
    # r = random.randint(1, 5)  # 1-5
    r = random.choice(items)
    # random.shuffle(items)
    print(items)
