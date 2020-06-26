"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

inp = input("Enter a sentence:")
lis = inp.split()
out = {}
for i in lis:
    if i in out:
        out[i] += 1
    else:
        out[i] = 1
print("Word count:", out)
