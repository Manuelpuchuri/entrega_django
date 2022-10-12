from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_de_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
