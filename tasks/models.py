from django.db import models


class UserPass(models.Model):
    username =  models.CharField(max_length=100, unique=True)
    email =  models.EmailField(unique=True, max_length=100)
    password =  models.CharField(max_length=100)
