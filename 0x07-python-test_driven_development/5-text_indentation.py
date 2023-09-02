#!/usr/bin/python3
"""
The text indentation module implements a function that
prints two newlines at the end of each statement that ends with
the following characters ['.', '?', ':']
"""
def text_indentation(text):
    """
    text_indentation - Prints two newlines after every "., ?, :"

    >>> text_indentation(123)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string
    
    """
    if not isinstance (text, str):
        raise TypeError("text must be a string")
    lines = []
    line = ""
    for c in text:
        line += c
        if c in ['.', '?', ':']:
            lines.append(line)
            line = ""
    for line in lines:
        print(f"{line.strip()}\n")