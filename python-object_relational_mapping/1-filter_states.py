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
    query = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(query)

    for row in cursor.fetchall():
        if (row[1][0] == 'N'):
            print(row)

    cursor.close()
    db.close()
