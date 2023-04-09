from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserPass(AbstractBaseUser):
    username =  models.CharField(max_length=100, unique=True)
    email =  models.EmailField(unique=True, max_length=100)
    password =  models.CharField(max_length=100)
    USERNAME_FIELD = 'username'
