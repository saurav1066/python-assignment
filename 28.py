"""
Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""

sample_dictionary = {}
key = input("Enter the key you wanna add:")
value = input("Enter the value:")
sample_dictionary[key] = value
print("key added successfully", sample_dictionary)
