"""

Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

"""


def my_sum(num1, num2):
    return num1+num2


num1, num2 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
print(my_sum(num1, num2))
