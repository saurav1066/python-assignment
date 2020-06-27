"""
Write a Python program to check whether a given string is number or not
using Lambda.
"""

inp = input("Enter a string")
num_check = lambda input_value : print("The given string is a number") if input_value.isnumeric() else print("not a number")
num_check(inp)
