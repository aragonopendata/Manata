from django.db import models

class Concedidas(models.Model):
    concedente = models.CharField(max_length=65000)
    beneficiario = models.CharField(max_length=65000)
    finalidad = models.CharField(max_length=65000)
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    norma = models.CharField(max_length=65000)
    orden = models.CharField(max_length=65000)
    ejercicio = models.IntegerField()
    importe_ejercicio = models.DecimalField(max_digits=12, decimal_places=2)
    modo_concesion = models.CharField(max_length=65000)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=65000)

    class Meta:
        db_table = 'subvenciones_concedidas'
        managed = False
