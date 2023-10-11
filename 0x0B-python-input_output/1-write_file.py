#!/usr/bin/python3

"""
Module containing a function to write a string to a text file (UTF8) and return
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file

    Parameters:
    filename (str): The name of the file to write to.
    text (str): The text to be written to the file.

    Returns:
    int: The number of characters written to the file.
    """
    # Open the file in write mode using the with statement
    with open(filename, 'w', encoding='utf-8') as file:
        # Write the text to the file and get the number of characters written
        num_chars_written = file.write(text)

    return num_chars_written
