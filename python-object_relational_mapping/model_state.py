#!/usr/bin/python3

"""
this is documented
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """this is the state table class"""
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)