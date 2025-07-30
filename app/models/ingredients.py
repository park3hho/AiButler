from __future__ import annotations  # Python 3.7 이상부터 가능
from tortoise import fields
from tortoise.models import Model


class IngredientModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    quantity = fields.FloatField()
    unit = fields.CharField(max_length=20)
    expiry_date = fields.DateField()
    stored_at = fields.DatetimeField(auto_now_add=True)

    user: fields.ForeignKeyRelation["UserModel"] = fields.ForeignKeyField(
        "models.UserModel", related_name="ingredients"
    )
    category: fields.ForeignKeyRelation["IngCategoryModel"] = fields.ForeignKeyField(
        "models.IngCategoryModel", related_name="ingredients"
    )

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"