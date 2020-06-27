"""
 Write a Python program to multiply all the items in a dictionary.
"""
dic2 = {3: 30, 4: 40}
mul_elements = 1
for i in dic2:
    mul_elements *= dic2[i]
print("the product is ", mul_elements)