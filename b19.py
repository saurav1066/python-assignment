"""
Write a Python program to create Fibonacci series upto n using Lambda.
"""
from functools import reduce

inp = int(input("Enter a number:"))

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])
print(f'fibonacci sequence {fib_series(inp)}')

"""
I have no idea how this worked...

"""