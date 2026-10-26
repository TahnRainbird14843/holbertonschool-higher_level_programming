#!/usr/bin/python3

"""
This file prints all rows form a given mysql database
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

    cursor = db.cursor()
    query = "SELECT cities.name FROM states " \
            "LEFT JOIN cities" \
            "ON cities.state_id = states.id" \
            "WHERE states.name = (%s)" \
            "ORDER BY cities.id ASC"

    cursor.execute(query, sys.argv[4])

    for row in cursor.fetchall():
        print(row[0], sep=', ')

    cursor.close()
    db.close()
