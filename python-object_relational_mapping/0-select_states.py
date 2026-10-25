import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) != 4:
        raise ValueError("Not enough arguments")

    db = MySQLdb.connect(host="localhost:3306", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    