#!/usr/bin/python3
"""
This file implements a program
that query the database htbn_0e_usa
"""
import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".
        format(user, password, database)
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    item = session.query(State).first()
    if item:
        print(item.id, item.name, sep=": ")
    else:
        print('Nothing')


if __name__ == "__main__":
    main()
