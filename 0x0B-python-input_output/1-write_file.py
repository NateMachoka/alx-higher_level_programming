#!/usr/bin/python3

"""
Module containing a function to write a string to a text file (UTF8) and return
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters
written.

    Parameters:
    filename (str): The name of the text file to write to. Default is an
empty string.
    text (str): The string to be written to the file. Default is empty string

    Returns:
    int: The number of characters written to the file.
    """

    with open(filename, 'w', encoding='utf-8') as file:
            char_count = file.write(text)
            return char_count
    except PermissionError:
        print(f"Permission denied: Cannot write to '{filename}'")
        return -1

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0
