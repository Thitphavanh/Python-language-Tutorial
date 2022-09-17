# Factorial Function
def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)


x=factorial(8)
print(x)


''''
5! = 5 x 4 x 3 x 2 x 1 = 120
5! 
5
5 x factorial(4)
5 x factorial(3)
5 x factorial(2)
5 x factorial(1)
5 x 4 x 3 x 2 x 1 = 120

'''
