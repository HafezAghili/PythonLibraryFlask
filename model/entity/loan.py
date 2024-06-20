from model.entity.base import *
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    loandate = Column(DateTime)

    def __init__(self, book_id, user_id):
        self.id = None
        self.book_id = book_id
        self.user_id = user_id
        self.loandate = datetime.datetime.now()

# class Loan(Base):
#     __tablename__ = 'loans'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     book_id = Column(Integer, ForeignKey('books.id'), unique=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     loandate = Column(DateTime)
#     book = relationship("Book", backref="loan")
#     user = relationship("User", backref="loans")

#     def __init__(self, book_id, user_id):
#         self.id = None
#         self.book_id = book_id
#         self.user_id = user_id
#         self.loandate = datetime.now()