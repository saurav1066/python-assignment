"""
Write a Python script to check whether a given key already exists in a
dictionary.
"""


def check_key(dictionary, myKey):
    if myKey in dictionary:
        print("key already exists.")
    else:
        print("this is a new key")


dic = {1: "apple", 2: "ball", 3: "cat", 4: "dog"}
k_ey = 7
check_key(dic, k_ey)
