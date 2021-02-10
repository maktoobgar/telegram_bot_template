import sys
from django.db import models


# User Model
class User(models.Model):
    name = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name
