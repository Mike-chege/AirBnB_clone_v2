#!/usr/bin/python3
"""
The Class User Module
"""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Class User Definition
    Defines the user for the MySQL database
    It contains all the information about that the user uses to login
    __tablename__ : The MySQL table to store the user info
    email: The user's email address
    password: The user's password
    first_name: The user's first name
    last_name: The user's last name
    places: The relationship between the user and the place
    reviews: The reviews made by the user
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
