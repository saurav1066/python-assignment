"""
Write a Python program to sum all the items in a list.
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
out = 0
for i in range(inp):
    val = int(input("Enter list elements:"))
    lis += [val]
for i in lis:
    out += i
print("The sum is:", out)
