"""
Write a Python program that takes a list of words and returns the length of the longest one.
"""

inp = int(input("Enter the number of items in the list:"))
list_words = []
out = ""

for i in range(inp):
    list_elements = input("Enter the list element:")
    list_words += [list_elements]
for i in list_words:
    if len(out) < len(i):
        out = i
print("The length of longest element is: ", len(out))
