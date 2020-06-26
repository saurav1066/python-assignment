"""
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""


def insert_string_middle(cover, content):
    out = cover[0:len(cover) // 2] + content + cover[len(cover) // 2:]
    return out


cover_value = input("Enter the cover for string:")
content_value = input("Enter content:")
output = insert_string_middle(cover_value, content_value)
print(output)
