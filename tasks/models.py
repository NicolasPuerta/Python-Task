from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserPass(AbstractBaseUser):
    username =  models.CharField(max_length=100, unique=True)
    email =  models.EmailField(unique=True, max_length=100)
    password =  models.CharField(max_length=100)
    USERNAME_FIELD = 'username'


class Task(models.Model):
    IMPORTANT_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True,blank=True)
    important = models.CharField(max_length=1, choices=IMPORTANT_CHOICES)
    user = models.ForeignKey(UserPass, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title