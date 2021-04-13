from django.db import models


# User Model
class User(models.Model):
    userid = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=32, default='', blank=True, null=True)

    def __str__(self):
        return self.userid