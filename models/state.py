#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column, Integer, String, DateTime


from models.city import City
from sqlalchemy.orm import relationship
import os

type1 = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if type1 == 'db':
        cities = relationship('City', backref="state",
                              cascade="all, delete",
                              passive_deletes=True)
    else:
        @property
        def cities(self):
                """get cities with same state_id as state"""
                from models.__init__ import storage
                list1 = []
                for k, v in storage.all(City).items():
                        if (v.state_id == self.id):
                                list1.append(v)
                return list1
