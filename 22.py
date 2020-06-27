"""
Write a Python program to remove duplicates from a list.
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
out = []
count = 0
for i in range(inp):
    val = input("Enter list elements:")
    lis += [val]
for i in lis:
    if i in out:
        pass
    else:
        out += [i]
print("Removing all the duplicate values:", out)
print("using set:", set(lis))


