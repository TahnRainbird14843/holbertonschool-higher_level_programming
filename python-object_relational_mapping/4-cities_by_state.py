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
    query = "SELECT cities.id, cities.name, states.name " \
            "FROM states " \
            "INNER JOIN cities " \
            "ON cities.state_id=states.id " \
            "ORDER BY cities.id ASC"

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
