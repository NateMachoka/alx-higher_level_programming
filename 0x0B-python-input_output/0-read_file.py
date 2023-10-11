#!/usr/bin/python3

"""
Module containing a function to read and print the contents of a text file.
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file (UTF8) to stdout.

    Parameters:
    filename (str): The name of the file to be read.

    Returns:
    None
    """
    # Open the file in read mode using the with statement
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the file line by line and print it to stdout
        for line in file:
            print(line, end='')
