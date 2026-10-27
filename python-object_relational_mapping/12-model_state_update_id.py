#!/home/tahn-rainbird/.pyenv/versions/3.8.20/bin/python
"""
this is documented
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, insert, update)
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
    stmt = update(State).where(State.id == 2).values(name="New Mexico")
    states = session.execute(stmt)
    session.commit()

    session.close()
