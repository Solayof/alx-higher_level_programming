#!/usr/bin/python3

"""State class that inherit from Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base


data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """
    class State with attribute id and name
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
