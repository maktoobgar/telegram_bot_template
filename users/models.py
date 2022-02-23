from django.db import models


# User Model
class User(models.Model):
    userid = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=32, default='', blank=True, null=True)
    first_name = models.CharField(max_length=64, default='', null=True)
    last_name = models.CharField(max_length=64, default='', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userid