from django.db import models
from django.core import validators

class User(models.Model, ):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, validators=[validators.EmailValidator()])
    password = models.CharField(max_length=50, validators=[validators.MinValueValidator(8)])


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(protocol="IPV4", default="0.0.0.0")

class Group(models.Model):
    name = models.CharField(max_length=50)


class Event(models.Model):
    ERROR_LEVEL = [
        ('CRITICAL', 'CRITICAL'),
        ('DEBUG', 'DEBUG'),
        ('ERROR', 'ERROR'),
        ('WARNING', 'WARNING'),
        ('INFO', 'INFO'),
    ]
    level = models.CharField(max_length=20, choices=ERROR_LEVEL)
    data = models.TextField()
    arquivado = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class GroupUser(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


