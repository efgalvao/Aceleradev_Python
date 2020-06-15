from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# OLD
from django.core import validators

class User2(models.Model, ):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último login', auto_now_add=True)
    email = models.EmailField('E-mail', max_length=254, unique=True)
    password = models.CharField('Senha', max_length=50, validators=[validators.MinLengthValidator(8)])

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.GenericIPAddressField('Origem', protocol="IPV4", default="0.0.0.0")

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    ERROR_LEVEL = [
        ('CRITICAL', 'CRITICAL'),
        ('DEBUG', 'DEBUG'),
        ('ERROR', 'ERROR'),
        ('WARNING', 'WARNING'),
        ('INFO', 'INFO'),
    ]
    level = models.CharField(max_length=20, choices=ERROR_LEVEL)
    data = models.TextField("Dados")
    arquivado = models.BooleanField('Arquivado', default=False)
    date = models.DateField('Data', auto_now=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.data
class GroupUser(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# TESTE
class Error(models.Model):
    ERROR_LEVEL = [
        ('CRITICAL', 'CRITICAL'),
        ('DEBUG', 'DEBUG'),
        ('ERROR', 'ERROR'),
        ('WARNING', 'WARNING'),
        ('INFO', 'INFO'),
    ]
    level = models.CharField(max_length=20, choices=ERROR_LEVEL)
    title = models.CharField("Titulo do erro", max_length=100)
    details = models.TextField("Detalhes")
    address = models.GenericIPAddressField('Address', protocol="IPV4", default="0.0.0.0")
    date = models.DateTimeField('Último login', auto_now_add=True)
