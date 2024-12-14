from django.db import models

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    numero_personas = models.IntegerField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha_reserva} {self.hora_reserva}"
