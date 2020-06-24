"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to
'$', except the first char itself.

Sample String : 'restart'
Expected Result : 'resta$t'
"""

inp = input("Enter the string:")
out = ''
lis = [inp[0]]
for i in inp[1:len(inp):1]:
    if i == lis[0]:
        lis += ["$"]
    else:
        lis += [i]

for i in lis:
    out += i
print(out)
