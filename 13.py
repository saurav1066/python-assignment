"""
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted
form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black,black, green, red, white
"""

inp = input("Enter input separated with comma:")
lis = inp.split(sep=",")
lis.sort()
print(lis)
