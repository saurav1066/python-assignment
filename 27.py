"""
 Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""


def take_list():
    inp = int(input("Enter total number of elements in the list:"))
    lis = []
    for i in range(inp):
        val = input("Enter list elements:")
        lis += [val]
    return lis


first_list = take_list()
second_list = take_list()
out = first_list[0:-1] + second_list
print(out)
