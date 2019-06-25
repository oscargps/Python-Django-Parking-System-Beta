from django.db import models
from apps.owners.models import Owner
# Create your models here.
class Car(models.Model):
    tipo=models.CharField(max_length=50)
    placa= models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    fecha_in=models.DateField()
    fecha_out=models.DateField()
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete= models.CASCADE)
