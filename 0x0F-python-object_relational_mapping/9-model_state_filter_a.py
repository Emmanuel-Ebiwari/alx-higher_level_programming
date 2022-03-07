#!/usr/bin/python3
"""
 lists all State objects that contain the letter a from the database
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
    orm_query = session.query(State).filter(State.name.like(
                                            "%a%")).order_by(State.id)
    for state in orm_query:
        print("{}: {}".format(state.id, state.name))
    session.close()
