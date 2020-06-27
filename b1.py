"""
Write a Python function to find the Max of three numbers.
"""


def max_finder(a, b, c):
    if a > b and a > c:
        print(f'{a} is largest')
    elif b > a and b > c:
        print(f'{b} is largest')
    else:
        print(f'{c} is largest')


