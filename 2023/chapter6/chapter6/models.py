from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField


class score(models.Model):
    kh = CharField(max_length=20)
    name = CharField(max_length=20)
    chinese = IntegerField()
    math = IntegerField()
    english = IntegerField()

    def __str__(self):
        return self.name
