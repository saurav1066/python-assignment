"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""

inp = input("Enter two strings with a space:")
intermediate_input = inp.split()
lista = []
listb = []
out = ''
put = ''
for i in intermediate_input:
    swap = i[0:2]
    constant = i[2:]
    lista += [swap]
    listb += [constant]
lista.reverse()
for i, j in lista, listb:
    out += i
    put += j
print(out, put)
