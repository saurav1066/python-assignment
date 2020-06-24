"""
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

inp = input("Enter a string:")
out = ''
if len(inp) < 3:
    raise Exception("length of string should be greater than 3")
else:
    if inp[-3:] == "ing":
        out += inp+"ly"
    else:
        out += inp+"ing"
print(out)
