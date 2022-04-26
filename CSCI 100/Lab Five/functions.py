# 0) Write a function named double which has one parameter,
#    and returns that parameter doubled.
#
# e.g double(7) -> 14
#     double(-9) -> -18


def double(num):
    return num * 2


# 1) Write a function named is_negative which has one parameter,
#    and returns True if the parameter is a negative value.
#
# e.g. is_negative(99) -> False
#      is_negative(-4.5) -> True
#      is_negative(0) -> False

def is_negative(num):
    if (num <= -1):
        return True
    else:
        return False


# 2) Write a function called product_and_two which takes two
#    parameters and returns the product of the two values plus
#    two.
#
# e.g. product_and_two(4, 7) -> 30
#      product_and_two(10, 7) -> 72
#      product_and_two(9, 0) -> 2


def product_and_two(num1, num2):
    return (num1 * num2) + 2
    

# 3) Write a function called power which takes two parameters
#    and returns the first one raised to the power of the second
#    one.
#
#    Do not use the double * operator or the math pow function.
#
# e.g. power(2, 5) -> 32
#      power(4, 3) -> 64


def power(num1, num2):
    
    if num2 == 0:
        return 1
    res = num1
    for i in range(num2 - 1):
        res = res * num1
    
    return res



