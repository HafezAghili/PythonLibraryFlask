from model.data_access.data_access import DataAccess
from model.entity.user import User

user_da = DataAccess(User)

user1 = User("amir","messbah","Ahmad","ahmad","ahmad123", None)
user_da.save(user1)
print(user1)

name, cls, id, name, role, email, phone, password