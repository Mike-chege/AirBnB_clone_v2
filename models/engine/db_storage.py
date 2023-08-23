#!/usr/bin/python3
"""
The DBStorage Module
"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """
    The Class DBStorage
    Implements a database storage engine
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializing a new DBStorage instance
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Method all
        Makes a query on the curret database session
        all objects of the given class
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """
        Method new
        Adds a new obj to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Method save
        Savees all the changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Method delete
        Deletes obj from the current database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Method reload
        Creates all tables in the database
        And initializes a new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Method close
        Closes the working SQLAlchemy session
        """
        self.__session.close()
