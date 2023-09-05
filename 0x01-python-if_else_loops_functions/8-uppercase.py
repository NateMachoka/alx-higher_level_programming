#!/usr/bin/python3
def uppercase(input_str):
    for i in input_str:
        if "a" <= i <= "z":
            i = chr(ord(i) - ord("a") + ord("A"))
        print("{}".format(i), end="")
    print()
