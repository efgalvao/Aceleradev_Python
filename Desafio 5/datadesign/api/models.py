from django.db import models

# Create your models here.
class api_user(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField
    e-mail = models.CharField(max_length=254)
    password = models.CharField(max_length=50)

class api_agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    addres = models.CharField(max_length=39)

class api_group(models.Model):
    name = models.CharField(max_length=50)
    
class api_event(models.Model):
    level = models.CharField(max_length=20)
    data = models.TextField
    arquivado = models.BooleanField
    date = models.DateField
    agent_id = models.IntegerField
    user_id = models.IntegerField

class api_grouuser(models.Model):
    group = models.IntegerField
    user_id =models.IntegerField
    


# Modelos do Mozilla
'''
class MyModelName(models.Model):
    """Uma típica classe definindo um modelo, derivada da classe Model."""

    # Campos
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadados
    class Meta: 
        ordering = ['-my_field_name']

    # Métodos
    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """ String para representar o objeto MyModelName (no site Admin)."""
        return self.my_field_name
'''