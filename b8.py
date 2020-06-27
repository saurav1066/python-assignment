"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""


def list_filter(lis):
    out = []
    for i in lis:
        if i in out:
            continue
        else:
            out += [i]
    return out


inp = int(input("Enter the number of elements in the list:"))
lis = []
for i in range(inp):
    list_elements = input("Enter the list element:")
    lis += [list_elements]
output = list_filter(lis)
print(output)
