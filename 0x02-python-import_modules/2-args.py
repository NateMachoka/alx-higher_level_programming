#!/usr/bin/python3

import sys


def print_arguments(argv):
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument\n""1:", argv[0])
    else:
        print("{} arguments:".format(num_args))

        for i, arg in enumerate(argv, start=1):
            print("{0}: {1}".format(i, arg))


if __name__ == "__main__":
    argv = sys.argv[1:]
    print_arguments(argv)
