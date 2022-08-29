# Function *agrs
# def add(*args):
#     print(args)


# def add(*args):
#     print(args[0]+args[1])

# def add(*args):
#     sum = 0
#     for item in args:
#         sum += item
#     print(sum)


# def add(*args):
#     sum = 0
#     for i in range(len(args)):
#         sum += args[i]
#     print(sum)
    
def add(*number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    print(sum)


# add()
add(10, 20)
add(20, 30)
add(20, 30, 50, 100, 125, 250, 1000)
