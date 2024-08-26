from django.db import models

class habitaciones(models.Model):
    nombre_habitacion  = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __str__(self):
        return self.nombre_habitacion
