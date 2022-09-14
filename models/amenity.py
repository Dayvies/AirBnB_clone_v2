#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
type1 = os.getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Class on amenities"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    if type1 == 'db':
        place_amenities = relationship(
            'Place', secondary='place_amenity', back_populates='amenities')
