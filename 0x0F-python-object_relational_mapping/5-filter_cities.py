#!/usr/bin/python3

"""
Displays all cities of a state search in the database
"""

import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    WHERE states.name LIKE %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    for index, city in enumerate(cities):
        if index != len(cities) - 1:
            print(city[0], end=', ')
        else:
            print(city[0])

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
