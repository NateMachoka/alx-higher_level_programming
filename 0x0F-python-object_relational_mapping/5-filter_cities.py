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

    if cities:
        print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
