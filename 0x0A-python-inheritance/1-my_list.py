#!/usr/bin/python3

"""Module containing a custom list class with sorting functionality.
"""


class MyList(list):
    """A custom list class that inherits from the built-in list class.

    This class provides an additional method to print the list in sorted order.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        This method sorts the elements of the list in ascending order
        and then prints the sorted list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
