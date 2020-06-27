"""
Write a Python program to add an item in a tuple.
"""

sample_tuple = ('a', 'b', 'c')
lis = list(sample_tuple)
inp = input("Enter the element you want to add:")
lis.append(inp)
print(tuple(lis))

