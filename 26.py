"""
Write a Python program to insert a given string at the beginning of all items in
a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
out = []
for i in range(inp):
    val = input("Enter list elements:")
    lis += [val]
inp_string = input("Enter the string to insert at beginning of the list:")
for i in lis:
    i = inp_string + i
    out += [i]
print(out)
