"""
Write a Python program to get the smallest number from a list.
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
for i in range(inp):
    val = int(input("Enter list elements:"))
    lis += [val]
lis.sort()
print("The smallest number is:", lis[0])
