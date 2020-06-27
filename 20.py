"""
Write a Python program to count the number of strings where the string length is 2 or more and the first and last
character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

inp = int(input("Enter total number of elements in the list:"))
lis = []
count = 0
for i in range(inp):
    val = input("Enter list elements:")
    lis += [val]
for i in lis:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print("The count of the number of strings with length 2 or more and first and last character same: ", count)

