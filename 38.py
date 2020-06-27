"""
Write a Python program to remove a key from a dictionary.
"""

inp = int(input("Enter a number to generate dictionary:"))
out = {}
for i in range(1, inp+1):
    out[i] = i*i
key_remove = int(input("Enter the key you want to remove:"))
if key_remove in out:
    del out[key_remove]
    print("Key removed successfully", out)
else:
    print("Sorry the key does not exist to remove ")

