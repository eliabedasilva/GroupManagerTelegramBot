from datetime import datetime
from BaseModel import BaseModel, db
from peewee import CharField, IntegerField, DecimalField, DateField


class Subscription(BaseModel):
    duration = IntegerField(null=False)
    price = DecimalField(null=False)
    name = CharField(null=False)
    notification_days = IntegerField(null=False)

