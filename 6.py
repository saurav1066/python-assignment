"""
Write a python program to find the first appearance of the substring 'not' and'poor'
from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor
"""

inp = input("Enter a string:")
print(id(inp))
i = "not"
j = "poor"
index_i = inp.find(i)
index_j = inp.find(j)
if index_i < index_j:
    if i in inp:
        if j in inp:
            inp = inp[0:index_i] + "good" + inp[index_j + len(j):]
            print(id(inp))
print(inp)
