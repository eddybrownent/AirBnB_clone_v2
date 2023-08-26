#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        places: relationship to place
        reviews: relationship to review

    """

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
