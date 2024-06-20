from model.entity.base import *
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from model.entity.loan import Loan

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    role = Column(String)
    email = Column(String)
    phone = Column(Integer, unique=True)
    password = Column(String(20), nullable=False)
    joindate = Column(DateTime)
    loans = relationship(Loan, backref="user")

    def __init__(self, name, role, email, phone, password):
        self.id = None
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.password = password
        self.joindate = datetime.datetime.now()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String)
#     role = Column(String)
#     email = Column(String)
#     phone = Column(Integer, unique=True)
#     password = Column(String(20), nullable=False)
#     joindate = Column(DateTime)
#     loans = relationship("Loan", backref="user")

#     def __init__(self, name, role, email, phone, password):
#         self.id = None
#         self.name = name
#         self.role = role
#         self.email = email
#         self.phone = phone
#         self.password = password
#         self.joindate = datetime.now()