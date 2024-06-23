#!/usr/bin/python3

"""
Defines a State model
Inherits from SQLAlchemy Base and links to the MySQL table states
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for our class definitions
Base = declarative_base()


class State(Base):
    """State class to link to MySQL table 'states'"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
