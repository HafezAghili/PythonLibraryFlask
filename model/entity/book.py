from model.entity.base import *
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from model.entity import *
from datetime import datetime, timezone


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(Integer, unique=True)
    title = Column(String(50))
    author = Column(String(50))
    language = Column(String(50))
    pubdate = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, isbn, title, author, language, pubdate):
        self.id = None
        self.isbn = isbn
        self.title = title
        self.author = author
        self.language = language
        self.pubdate = datetime.now(timezone.utc)
        
# class Book(Base):
#     __tablename__ = 'books'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     isbn = Column(Integer, unique=True)
#     title = Column(String)
#     author = Column(String)
#     language = Column(String)
#     pubdate = Column(DateTime)
#     loan = relationship("Loan", backref="book", uselist=False)

#     def __init__(self, isbn, title, author, language, pubdate):
#         self.id = None
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.language = language
#         self.pubdate = pubdate