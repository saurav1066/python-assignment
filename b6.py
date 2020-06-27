"""
Write a Python function to check whether a number is in a given range
"""


def check_in_range(fro, to, num):
    if fro < num < to:
        print(f'{num} in range {fro} - {to} ')
    else:
        print("Out of range")


check_in_range(1, 5, 4)
