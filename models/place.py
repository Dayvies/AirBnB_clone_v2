#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models import storage
import os

type1 = os.getenv("HBNB_TYPE_STORAGE")

if type1 == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(
        'cities.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(String(60), ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if type1 == 'db':
        reviews = relationship('Review', backref="place",
                               cascade="all, delete",
                               passive_deletes=True)
        amenities = relationship(
            'Amenity', secondary='place_amenity', back_populates='place_amenities', viewonly=False)
    else:

        @property
        def cities(self):
            """get cities with same state_id as state"""
            list1 = []
            for k, v in storage.all(Review).items():
                if (v.place_id == self.id):
                    list1.append(v)
            return list1

        @property
        def amenities(self):
            """ instances based on the attribute amenity_ids"""
            list1 = []
            for id in self.amenity_ids:
                for k, v in storage.all(Amenity).items():
                    if (v.place_id == self.id):
                        list1.append(v)
            return list1

        @amenities.setter
        def amenities(self, obj):
            """setter on amenity_ids"""
            if (type(obj) == Amenity):
                self.amenity_ids.append(obj.id)
