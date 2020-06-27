"""
Write a Python program to convert a list to a tuple.
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
for i in range(inp):
    val = input("Enter list elements:")
    lis += [val]
print(f'list: {lis} tuple{tuple(lis)}')
