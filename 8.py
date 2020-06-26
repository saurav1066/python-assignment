"""
Write a Python program to remove the nth index character from a nonempty string.
"""

inp = input("Enter a string:")
remove_index = int(input("Enter the index you want to remove:"))

if len(inp) < remove_index:
    print("Sorry the string is shorter than you think.. ")

else:
    inp = inp[0:remove_index]+inp[remove_index+1:]
print(inp)
