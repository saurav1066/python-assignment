"""
Write a Python program to check whether all dictionaries in a list are empty or
not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""


def check_dict_in_list(lis):
    for i in lis:
        if bool(i):
            print("False")
            return 0
        else:
            continue
    print("True")


# lis = [{}, {}, {}]
# check_dict_in_list(lis)
