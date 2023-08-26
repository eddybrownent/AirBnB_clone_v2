#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
import models
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models

    Attributes:
        id (sqlachemy String): Basemodel id
        created_at (sqlalchemy Datetime): datetime at creation
        updated_at (sqlalchemy Datetime): datetime of last update
    """

    id = Column(String(60),
                nullable=False,
                primary_key=True)

    created_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())

    updated_at = Column(DateTime,
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                # Convert "created_at" and "updated_at" strings to datetime obj
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Converts object attributes to dictionary format"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in my_dict.keys():
            del my_dict["_sa_instance_state"]
        return my_dict

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def delete(self):
        """"delete the current instance from the storage (models.storage)"""
        models.storage.delete(self)
