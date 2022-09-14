#!/usr/bin/python3
"""This module defines a class to manage file storage via mysql"""
import sqlalchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
import json
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

user = os.getenv("HBNB_MYSQL_USER")
host = os.getenv("HBNB_MYSQL_HOST")
password = os.getenv("HBNB_MYSQL_PWD")
database = os.getenv("HBNB_MYSQL_DB")
env = os.getenv("HBNB_ENV")


class DBstorage:
    """mysql file storage"""
    __engine = None
    __session = None

    def __init__(self):
        """ initialising DBstorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)
        if env == 'test':
            meta = sqlalchemy.MetaData(self.__engine)
            meta.reflect()
            meta.drop_all()

    def all(self, cls=None):
        """returns declared class or everything"""

        dict1 = {}
        oblist = []
        if cls is None:

            for obj in self.__session.query(State).all():
                oblist.append(obj)
            for obj in self.__session.query(City).all():
                oblist.append(obj)
            for obj in self.__session.query(User).all():
                oblist.append(obj)
            for obj in self.__session.query(Place).all():
                oblist.append(obj)
            for obj in self.__session.query(Review).all():
                oblist.append(obj)
        else:
            for obj in self.__session.query(cls).all():
                oblist.append(obj)
        for obj in oblist:
                id = ("{}.{}".format(type(obj).__name__,obj.id))
                dict1.update({id:obj})
        return dict1

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current  session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is None:
            return
        self.__session.delete(obj)

    def reload(self):
        """reloading self and initiating storage"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
        