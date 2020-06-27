"""
 Write a Python program to find if a given string starts with a given character
using Lambda.
"""

inp = input("Enter a character")
inp_str = input("Enter a string")
character_checker = lambda string, character: True if string.startswith(character) else False
print(f'{inp_str} starts with {inp} {character_checker(inp_str, inp)}')