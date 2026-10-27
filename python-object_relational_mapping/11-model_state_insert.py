#!/usr/bin/python3
"""
this is documented
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, insert)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = insert(State).values(name="Louisiana")
    states = session.execute(stmt)
    session.commit()

    print(states.inserted_primary_key[0])

    session.close()
