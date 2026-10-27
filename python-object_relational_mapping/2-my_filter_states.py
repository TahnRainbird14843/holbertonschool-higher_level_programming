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
    query = "SELECT * FROM states " \
            "WHERE states.name = '{}' " \
            "ORDER BY states.id ASC;".format(sys.argv[4])

    cursor.execute(query)

    output = cursor.fetchall()

    if len(output) == 0:
        print("Not Found")
    else:
        for row in output:
            print(row)

    cursor.close()
    db.close()
