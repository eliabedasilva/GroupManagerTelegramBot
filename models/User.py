from datetime import datetime
from BaseModel import BaseModel, db
from peewee import IntegerField, CharField, DateField, BooleanField

class User(BaseModel):
    telegram_id = IntegerField(unique=True)
    telegram_name = CharField()
    subscription_end_date = DateField()
    acess_link = CharField()
    is_adm = BooleanField(default=False)

