#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store the True/False values
    result = []

    # Iterate through the elements in the input list
    for num in my_list:
        is_divisible = num % 2 == 0

        # Append True or False to the result list
        result.append(is_divisible)
    return result
