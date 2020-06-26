"""
Write a Python program to remove the characters which have odd index values of a given string.
"""

inp = input("Enter a string:")
out = ""
for i in inp:
    a = inp.find(i)
    if a % 2 == 0:
        out += i

print(out)




