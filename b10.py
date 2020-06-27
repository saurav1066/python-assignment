"""
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""


def list_filter(lis):
    out = []
    for i in lis:
        if (i % 2) == 0:
            out += [i]
    return out


inp = int(input("Enter the number of elements in the list:"))
lis = []
for i in range(inp):
    list_elements = int(input("Enter the list element:"))
    lis += [list_elements]
output = list_filter(lis)
print(output)
