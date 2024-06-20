from controller.exceptions.exceptions import NoBookError
from model.data_access.da import Da
from model.entity.book import Book


class BookDa(Da):
    def save(self, book):
        self.connect()
        self.cursor.execute("INSERT INTO books (isbn, title, author, language, pubdate) VALUES (%s, %s, %s, %s, %s)",
                            [book.isbn, book.title, book.author, book.language, book.pubdate])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM books")
        book_tuple_list = self.cursor.fetchall()
        self.disconnect()
        if book_tuple_list:
            book_list = []
            for book_tuple in book_tuple_list:
                book = Book(book_tuple[1], book_tuple[2], book_tuple[3], book_tuple[4], book_tuple[5])
                book.book_id = book_tuple[0]
                book_list.append(book)
            return book_list
        else:
            raise NoBookError
