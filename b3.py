"""
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""


def mul_list(lis):
    mul_elements = 1
    for i in lis:
        mul_elements *= i
    return mul_elements


sample_list = [8, 2, 3, -1, 7]
out = mul_list(sample_list)
print(out)
