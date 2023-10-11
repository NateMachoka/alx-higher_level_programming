#!/usr/bin/python3

"""Module for appending text to a file"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return the number of
characters added.

    Parameters:
    filename (str): The name of the file to append to.
    text (str): The text to be appended to the file.

    Returns:
    int: The number of characters added to the file.
    """
    # Open the file in append mode using the with statement
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
