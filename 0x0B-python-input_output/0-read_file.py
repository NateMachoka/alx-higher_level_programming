#!/usr/bin/python3

"""
Module containing a function to read and print the contents of a text file.
"""


def read_file(filename=""):
    """
    Read the contents of a text file and print them to stdout.

    Parameters:
    filename (str): The name of the text file to be read (UTF8).
Default is an empty string.

    Returns:
    None
    """

    try:
        # Open the file for reading with UTF-8 encoding
        with open(filename, 'r', encoding='utf-8') as file:
            # Iterate through each line in the file and print it
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
