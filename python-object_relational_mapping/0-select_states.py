#!/usr/bin/python3

import MySQLdb
import sys

"""
this is documented
"""


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
    