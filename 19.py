"""
Write a Python program to get the smallest number from a list.
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
for i in range(inp):
    val = int(input("Enter list elements:"))
    lis += [val]
out = lis[0]
for i in lis:
    if out > i:
        out = i
print("The smallest number is:", out)
