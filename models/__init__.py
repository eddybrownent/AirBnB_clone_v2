#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel

# Choose the storage engine based on value of HBNB_TYPE_STORAGE
if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
