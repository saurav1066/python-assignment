"""
Write a Python program to square and cube every number in a given list of
integers using Lambda.
"""

sample_list = [1, 2, 3, 4, 5]
square = lambda num: num ** 2
cube = lambda num: num ** 3

square_list = list(map(square, sample_list))
cube_list = list(map(cube, sample_list))

print(square_list)
print(cube_list)
