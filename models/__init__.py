#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBstorage
import os

type1 = os.getenv("HBNB_TYPE_STORAGE")
if type1 == "db":
    storage = DBstorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
