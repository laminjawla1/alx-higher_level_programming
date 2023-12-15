#!/usr/bin/python3
"""
This file implements the base model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, MetaData)


metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """
    The state model - A blue print for State objects
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
