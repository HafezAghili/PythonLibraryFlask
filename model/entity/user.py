from model.entity.base import *
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from model.entity.loan import Loan
from model.entity import *

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    role = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50), unique=True)
    password = Column(String(20), nullable=False)
    joindate = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    loans = relationship('Loan', backref='user_loans')

    def __init__(self, name, role, email, phone, password):
        self.id = None
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.password = password
        self.joindate = datetime.now(timezone.utc)

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