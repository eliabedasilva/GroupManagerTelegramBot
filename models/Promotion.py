from datetime import datetime
from BaseModel import BaseModel, db
from peewee import CharField, IntegerField, DecimalField, DateField

class Promotion(BaseModel):
    name = CharField(null=False)
    subscription_promotion_duration = IntegerField(null=False)
    price = DecimalField(null=False)
    start_promotion_date = DateField(null=False)
    end_promotion_date = DateField(null=False)


