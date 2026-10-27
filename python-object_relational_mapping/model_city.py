#!/usr/bin/python3
"""
this has the city class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """this is the city class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states"), nullable=False)
