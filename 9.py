"""
 Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
"""
inp = input("Enter a  string:")
inp = inp[-1] + inp[1:len(inp)-1] + inp[0]
print(inp)