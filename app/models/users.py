from tortoise import fields
from tortoise.models import Model
from .ingredients import Ingredient

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=255, unique=True)
    ingredients: fields.ReverseRelation["Ingredient"]

    def __str__(self):
        return self.name
