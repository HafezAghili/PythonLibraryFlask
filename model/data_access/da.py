from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base

username = "root"
password = "@Mir1379"
database_name = "Library"

connection_string = f"mysql+pymysql://{username}:{password}@localhost:3306/{database_name}"

if not database_exists(connection_string):
    create_database(connection_string)


class Da:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Mir1379",
            database="mft"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
