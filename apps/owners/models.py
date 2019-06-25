from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=12)
    mail=models.EmailField()
    cedula=models.IntegerField()
    def __str__(self):
        return '{}'.format(self.nombre)