#!/usr/bin/python3
"""
This script describes the DBStorage engine
"""

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """
    Defines a database storage engine

    Attributes:
        __engine (sqlalchemy.Engine): The SQLAlchemy engine
        --session (sqlalchemy.Session): The SQLAlchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialises a DBStorage instance
        """

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        d_base = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, d_base),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query the database session fro objects of a given class

        Args:
            cls (class, optional): The class to query
                                If None, queries all types of objects

        Returns:
             dict: A dictionary of queried objects
                    format <class name>.<obj id> = obj
        """

        query_obj = {}
        all_classes = [State, City, User, Place, Review, Amenity]
        if cls is None:
            for cls in all_classes:
                objs = self.__session.query(cls)
                for obj in objs:
                    key = "{}.{}".format(cls.__name__, obj.id)
                    query_obj[key] = obj
        else:
            for cls in all_classes:
                objs = self.__session.query(cls)
                for obj in objs:
                    key = "{}.{}".format(cls.__name__, obj.id)
                    query_obj[key] = obj
        return query_obj

    def new(self, obj):
        """
        Adds an obj to current the database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"
        Creates all table in the databse and intiliazes a session
        """

        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create a session factory and use scoped_session for thread safety
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)

        # Initializing the session
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
