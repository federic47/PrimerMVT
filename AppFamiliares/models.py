from django.db import models

# Create your models here.
class Familiar(models.Model):
    numeroDeFamiliar = models.IntegerField()
    nombreYapellido = models.CharField(max_length=50)
    fechaNacimiento = models.CharField(max_length=50)

def __str__(self):
    return f'{self.numeroDeFamiliar}{self.nombreYapellido}{self.fechaNacimiento}'