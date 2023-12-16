#!/usr/bin/python3
"""
This file implements a program
that query the database htbn_0e_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".
        format(user, password, database),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id)

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.states.name))


if __name__ == "__main__":
    main()
