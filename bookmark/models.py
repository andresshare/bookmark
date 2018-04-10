from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Bookmark(models.Model):
    name = models.CharField(max_length=50)
    url =  models.URLField()
    ispublic = models.BooleanField(default=True)
    datetimeposted = models.DateTimeField(auto_now=True,verbose_name="posted_at")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return  self.name

