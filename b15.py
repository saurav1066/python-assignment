"""
Write a Python program to filter a list of integers using Lambda.
"""

sample_lit = [1, 2, 3, 4, 5]
even_finder = lambda num: num % 2 == 0
a = list(filter(even_finder, sample_lit))
print(a)
