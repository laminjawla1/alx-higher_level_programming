#!/usr/bin/python3
"""
This module implements the City Model
"""
from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """
    The City model
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
