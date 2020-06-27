"""
Write a Python program to get the largest number from a list.
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
out = 0
for i in range(inp):
    val = int(input("Enter list elements:"))
    lis += [val]
lis.sort()
print("The largest number is:", lis[-1])
