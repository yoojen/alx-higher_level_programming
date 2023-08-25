#!/usr/bin/python3
""" script that changes the name of a State object from the database hbtn_0e_6_usa"""
import MySQLdb
from model_state import Base, State
from sqlalchemy import create _engine
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id = 2).first()
    state.name = "New Mexico"
    state.commit()
