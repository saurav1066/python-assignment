"""
Write a Python program to create Fibonacci series upto n using Lambda.
"""

inp = int(input("Enter a number:"))
fibo = lambda num: num if num <= 1 else fibo(num-1)+fibo(num-2)
fibo_getter = list(map(fibo, range(0, inp)))
print(fibo_getter)
