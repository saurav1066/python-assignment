# Write a Python program to count the number of characters
# (character frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

inp = input("Enter a string:")
out = {}
for i in inp:
    if i in out:
        out[i] += 1
    else:
        out[i] = 1

print(out)
