"""
Write a Python program to sort a list of dictionaries using Lambda.
"""

lis = [{"name": "Saurav", "age": 23}, {"name": "sujan", "age": 12}, {"name": "Hitesh", "age": 15}]
value_fetch = lambda i: i['age']
print(sorted(lis, key=value_fetch))
