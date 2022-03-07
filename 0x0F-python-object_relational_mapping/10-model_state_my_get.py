#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    orm_query = session.query(State).filter(State.name == argv[4]).all()
    if orm_query:
        print("{}".format(orm_query[0].id))
    else:
        print("Not found")
    session.close()
