#!/usr/bin/python3
"""
This file implements a program
that query the database htbn_0e_usa
"""
import sys
from model_state import Base, State
from model_city import City
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

    states = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id)
    for state in states:
        print("{}: ({}) {}".format(state[0], state[1], state[2]))


if __name__ == "__main__":
    main()
