"""
 Write a Python function to create the HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""


def add_tags(tag, content):
    print("<"+tag+">", content, "</"+tag+">")


inp_tag = input("Enter tag:")
inp_content = input("Enter Content:")
add_tags(inp_tag, inp_content)
