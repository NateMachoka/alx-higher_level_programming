#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()

    sum_of_unique_integers = 0

    for num in my_list:
        if num not in unique_integers:
            unique_integers.add(num)
            sum_of_unique_integers += num

    return sum_of_unique_integers
