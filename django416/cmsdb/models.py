from django.db import models

# Create your models here.
class Usertype(models.Model):
    name = models.CharField(max_length=32)

class Userinfo(models.Model):
    username = models.CharField(max_length=30)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    user_type = models.ForeignKey(Usertype)