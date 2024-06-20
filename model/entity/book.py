from model.entity.base import *
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, back_populates


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(Integer, unique=True)
    title = Column(String)
    author = Column(String)
    language = Column(String)
    pubdate = Column(DateTime)

    def __init__(self, isbn, title, author, language, pubdate):
        self.id = None
        self.isbn = isbn
        self.title = title
        self.author = author
        self.language = language
        self.pubdate = pubdate
        
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