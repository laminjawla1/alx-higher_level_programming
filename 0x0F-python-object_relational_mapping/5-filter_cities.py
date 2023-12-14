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
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", user=user, passwd=password, db=database, port=3306
    )

    cur = db.cursor()

    cur.execute("""
        SELECT cities.name FROM cities INNER JOIN
        states ON states.id=cities.state_id
        WHERE states.name LIKE %s""", (state,))

    rows = cur.fetchall()

    print(*[row[0] for row in rows], sep=', ')
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
