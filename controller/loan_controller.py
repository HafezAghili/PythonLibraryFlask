from sqlalchemy import and_
from model.data_access.data_access import DataAccess
from model.entity import Loan, Book, User
from model.tools.decorators import exception_handling

class LoanController:
    loan_da = DataAccess(Loan)
    book_da = DataAccess(Book)
    user_da = DataAccess(User)

    @classmethod
    @exception_handling
    def can_borrow_book(cls, user_id):
        # تعداد کتاب‌های قرض گرفته شده توسط کاربر را بررسی کنید
        loans_count = cls.loan_da.find_all().filter(Loan.user_id == user_id).count()
        return loans_count < 2

    @classmethod
    @exception_handling
    def save(cls, book_id, user_id):
        # بررسی اینکه آیا کتاب قبلاً قرض داده شده است
        loan_exists = cls.loan_da.find_by(Loan.book_id == book_id)
        if loan_exists:
            return False, "This book is already loaned."

        # بررسی اینکه آیا کاربر می‌تواند کتاب دیگری قرض بگیرد
        if not cls.can_borrow_book(user_id):
            return False, "User cannot borrow more than 2 books."

        loan = Loan(book_id=book_id, user_id=user_id)
        return True, cls.loan_da.save(loan)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.loan_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.loan_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.loan_da.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_user_id(cls, user_id):
        return True, cls.loan_da.find_by(Loan.user_id == user_id)

    @classmethod
    @exception_handling
    def find_by_book_id(cls, book_id):
        return True, cls.loan_da.find_by(Loan.book_id == book_id)
