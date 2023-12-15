#!/usr/bin/python3
"""
This file implements a program
that query the database htbn_0e_usa
"""
import sys
import MySQLdb


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    query = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", user=user, passwd=password, db=database, port=3306
    )

    cur = db.cursor()

    cur.execute("""
                SELECT * FROM states WHERE name LIKE %s
                ORDER BY states.id ASC""", (query,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
