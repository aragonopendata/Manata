from django.db import models

class Concedidas(models.Model):
    concedente = models.ForeignKey('Concedentes')
    beneficiario = models.ForeignKey('Beneficiarios')
    finalidad = models.ForeignKey('Finalidades')
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    norma = models.ForeignKey('Normas')
    orden = models.ForeignKey('Ordenes')
    ejercicio = models.IntegerField()
    importe_ejercicio = models.DecimalField(max_digits=12, decimal_places=2)
    modo_concesion = models.ForeignKey('ModoConcesiones')
    fecha = models.DateField()
    descripcion = models.CharField(max_length=65000)

    class Meta:
        db_table = 'subvenciones_concedidas'
        managed = False


class Concedentes(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'concedentes'
        managed = False

    def __str__(self):
        return self.name


class Beneficiarios(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'beneficiarios'
        managed = False


class Finalidades(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'finalidades'
        managed = False


class Normas(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'normas'
        managed = False


class Ordenes(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'ordenes'
        managed = False


class ModoConcesiones(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'modo_concesiones'
        managed = False


class Convocadas(models.Model):
    seccion = models.CharField(max_length=65000)
    subseccion = models.CharField(max_length=65000)
    rango = models.ForeignKey('Rangos')
    emisor = models.ForeignKey('Emisores')
    titulo = models.CharField(max_length=65000)
    texto = models.CharField(max_length=2000000000)
    urlpdf = models.CharField(max_length=650000)
    fecha = models.DateField()

    class Meta:
        db_table = 'subvenciones_convocadas'
        managed = False


class Rangos(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'rangos'
        managed = False


class Emisores(models.Model):
    name = models.CharField(max_length=65000)

    class Meta:
        db_table = 'emisores'
        managed = False

