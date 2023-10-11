#!/usr/bin/python3

"""Module for inserting a line of text to a file after each line containing a
specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text to a file after each line containing specific string.

    Parameters:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert.

    Returns:
        None
    """
    # Open the input file for reading and a temporary file for writing
    with open(filename, 'r') as file, open(filename + '.tmp', 'w') as tmp_file:
        for line in file:
            # Write the current line from the input file to the temporary file
            tmp_file.write(line)
            # Check if the search string is present in the line
            if search_string in line:
                # Insert the new line after the line containing search string
                tmp_file.write(new_string)
                # Replace the original file with the temporary file
    import os
    os.rename(filename + '.tmp', filename)
