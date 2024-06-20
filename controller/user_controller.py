from sqlalchemy import and_
from model.data_access.data_access import DataAccess
from model.entity.user import User
from model.tools.decorators import exception_handling

class UserController:
    user_da = DataAccess(User)

    @classmethod
    @exception_handling
    def save(cls, name, role, email, phone, password):
        user = User(name=name, role=role, email=email, phone=phone, password=password)
        return True, cls.user_da.save(user)

    @classmethod
    @exception_handling
    def edit(cls, id, name, role, email, phone, password):
        user = cls.user_da.find_by_id(id)
        if user:
            user.name = name
            user.role = role
            user.email = email
            user.phone = phone
            user.password = password
            return True, cls.user_da.edit(user)
        return False, None

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, cls.user_da.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.user_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.user_da.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_username(cls, name):
        return True, cls.user_da.find_by(User.name == name)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, name, password):
        user = cls.user_da.find_by(and_(User.name == name, User.password == password))
        if user:
            return True, user
        return False, None
