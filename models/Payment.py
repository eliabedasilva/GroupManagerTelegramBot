from datetime import datetime
from BaseModel import BaseModel, db
from User import User
from peewee import ForeignKeyField, DecimalField, DateField, CharField

class Payment(BaseModel):
    user = ForeignKeyField(User, backref='payments')
    amount = DecimalField()
    payment_date = DateField(default=datetime.now())
    status = CharField(default='pending')


