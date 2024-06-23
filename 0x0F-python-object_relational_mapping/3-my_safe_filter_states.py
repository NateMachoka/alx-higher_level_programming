#!/usr/bin/python3

"""
Script for displaying searched names that's safe from injections
"""

import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close
    db.close


if __name__ == "__main__":
    main()
