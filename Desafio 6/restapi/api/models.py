from django.db import models

# Create your models here.

class Question(models.Model):
    quest = models.CharField(max_length=40)

