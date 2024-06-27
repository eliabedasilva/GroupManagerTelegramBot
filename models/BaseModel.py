from peewee import Model, MySQLDatabase
from credentials import DATABASE, HOST, PASSWORD, PORT, USER
db = MySQLDatabase(database=DATABASE, host=HOST, port=PORT, user=USER, password=PASSWORD)

class BaseModel(Model):
    class Meta:
        database = db
