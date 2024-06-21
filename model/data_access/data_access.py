import urllib.parse
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base

username = "root"
password = "@Mir1379"
database_name = "Library"

encoded_password = urllib.parse.quote_plus(password)

connection_string = f"mysql+pymysql://{username}:{encoded_password}@localhost:3306/{database_name}"

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
# Base.metadata.drop_all(engine) # todo
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class DataAccess:
    def __init__(self, model):
        self.model = model

    def save(self, entity):
        with Session() as session:
            session.add(entity)
            session.commit()
        return entity

    def edit(self, entity):
        with Session() as session:
            session.merge(entity)
            session.commit()
        return entity

    def remove(self, entity_id):
        with Session() as session:
            entity = session.query(self.model).get(entity_id)
            if entity:
                session.delete(entity)
                session.commit()
                return entity
        return None

    def find_by_id(self, entity_id):
        with Session() as session:
            return session.query(self.model).get(entity_id)

    def find_all(self):
        with Session() as session:
            return session.query(self.model).all()

    def find_by(self, *criterion):
        with Session() as session:
            return session.query(self.model).filter(*criterion).all()



# class DataAccess:
#     def __init__(self, class_name):
#         self.class_name = class_name
#         Base.metadata.create_all(bind=engine)

#     def save(self, entity):
#         session.add(entity)
#         session.commit()
#         session.refresh(entity)
#         return entity

#     def edit(self, entity):
#         session.merge(entity)
#         session.commit()
#         return entity

#     def remove(self, entity):
#         session.delete(entity)
#         session.commit()
#         return entity

#     def find_all(self):
#         entity_list = session.query(self.class_name).all()
#         return entity_list

#     def find_by_id(self, id):
#         entity = session.get(self.class_name, id)
#         return entity

#     def find_by(self, find_statement):
#         entity = session.query(self.class_name).filter(find_statement).all()
#         return entity
