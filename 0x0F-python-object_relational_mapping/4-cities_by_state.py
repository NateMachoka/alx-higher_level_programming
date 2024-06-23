#!/usr/bin/python3

"""
Module that lists all cities from the database
"""

import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name FROM cities
    JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close
    db.close


if __name__ == "__main___":
    main()
