from tortoise import fields
from tortoise.models import Model
from .ingredients import Ingredient

class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    ingredients: fields.ReverseRelation["Ingredient"]

    def __str__(self):
        return self.name
