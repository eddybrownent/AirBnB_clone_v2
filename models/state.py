#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        # id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan',  foreign_keys='City.state_id')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)


    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Get a list of all related City objects."""
            from models import storage
            city_list = []
            city_dict = storage.all(City)
            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
