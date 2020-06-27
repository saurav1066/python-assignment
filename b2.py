"""
 Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
"""


def sum_list(lis):
    sum_elements = 0
    for i in lis:
        sum_elements += i
    return sum_elements


sample_list = [8, 3, 2, 0, 7]
out = sum_list(sample_list)
print(out)
