"""
Write a Python program to clone or copy a list.
"""
inp = int(input("Enter total number of elements in the list:"))
lis = []
copied_list = []
for i in range(inp):
    val = input("Enter list elements:")
    lis += [val]
copied_list = lis.copy()
print("original:", lis)
print("Copied:", copied_list)
