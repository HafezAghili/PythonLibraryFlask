from model.entity.base import *
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from model.entity import *

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    loandate = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = relationship('User', backref='loan_user')
    book = relationship('Book', backref='loan_book')

    def __init__(self, book_id, user_id, loandate):
        self.id = None
        self.book_id = book_id
        self.user_id = user_id
        self.loandate = datetime.now(timezone.utc)

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