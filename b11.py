"""
Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result.
"""

sum_lambda = lambda num: num + 15
print(sum_lambda(7))

mul_lambda = lambda x, y: x * y
print(mul_lambda(6, 7))
