from model.data_access.data_access import DataAccess
from model.entity import Book
from model.tools.decorators import exception_handling

class BookController:
    book_da = DataAccess(Book)

    @classmethod
    @exception_handling
    def save(cls, isbn, title, author, language, pubdate):
        book = Book(isbn=isbn, title=title, author=author, language=language, pubdate=pubdate)
        return True, cls.book_da.save(book)

    @classmethod
    @exception_handling
    def edit(cls, id, isbn, title, author, language, pubdate):
        book = cls.book_da.find_by_id(id)
        if book:
            book.isbn = isbn
            book.title = title
            book.author = author
            book.language = language
            book.pubdate = pubdate
            return True, cls.book_da.edit(book)
        return False, None

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.book_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.book_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.book_da.find_by_id(id)
    
    @classmethod
    @exception_handling
    def find_by_isbn(cls, isbn):
        return True, cls.book_da.find_by(Book.isbn == isbn)
