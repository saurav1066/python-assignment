"""
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""


def reverse_string(inp_string):
    output = ""
    for i in range(len(inp_string)):
        output += inp_string[len(inp_string) - 1 - i]
    return output


a = reverse_string("1234abcd")
print(a)
