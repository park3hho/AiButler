from tortoise import fields
from tortoise.models import Model


class UserModel(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=100)
    name = fields.CharField(max_length=100)

    def __str__(self):
        return self.name
