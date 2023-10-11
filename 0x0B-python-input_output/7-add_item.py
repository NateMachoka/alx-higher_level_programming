#!/usr/bin/python3

"""Module for adding arguments to a list and saving it to a JSON file"""

import sys
import json
# Import the save_to_json_file and load_from_json_file functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []

    # Add command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to add_item.json as a JSON representation
    save_to_json_file(items, 'add_item.json')


if __name__ == '__main__':
    main()
