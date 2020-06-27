"""
 Write a Python program to find intersection of two given arrays using
Lambda.
"""

arrayA = [1,2,3,4,5,6]
arrayB=[4,5,6,7,8]
output = filter(lambda x: x in arrayA, arrayB)
print(list(output))
