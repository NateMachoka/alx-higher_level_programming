#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_value = my_list[0]  # Initialize max_value with the first element

    for num in my_list:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found

    return max_value
