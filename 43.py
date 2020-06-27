"""
Write a Python program to remove an item from a tuple.
"""

sample_tuple = ('a', 'p', 'p', 'l', 'e')
inp = input("Enter element u wanna remove:")
lis = list(sample_tuple)
if inp in lis:
    lis.remove(inp)
    print("Removed successfully")
else:
    print("item does not exist")

print(tuple(lis))
