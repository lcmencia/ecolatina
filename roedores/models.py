from django.db import models
from usuario.models import *
import datetime
from django.contrib.auth.models import User


class Estacion(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    propiedad = models.IntegerField(editable = False)
    cliente = models.IntegerField(editable = False)
    usuario = models.IntegerField(editable = False)
    fecha = models.DateTimeField(blank=True, null=True)
    instalador = models.ManyToManyField(Funcionario)
    
    class Meta:
        verbose_name_plural = "Estaciones"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        _cebo = self.sector
        _sector = Sector.objects.get(pk=_cebo.id)
        _propiedad = _sector.propiedad
        self.propiedad = _propiedad.id
        _cliente = _propiedad.cliente
        self.cliente = _cliente.id
        _Cliente = Cliente.objects.get(pk=_cliente.id)
        self.usuario = _Cliente.usuario.id
        super(Estacion, self).save(*args, **kwargs)

class Estado(models.Model):
    nombre = models.CharField(unique=True ,max_length=255)
    descripcion = models.TextField()
    class Meta:
        verbose_name_plural = "Estados"

    def __str__(self):
        return '%s' % (self.nombre)

class Accion(models.Model):
    nombre = models.CharField(unique=True ,max_length=255)
    descripcion = models.TextField()
        
    class Meta:
        verbose_name_plural = "Acciones"

    def __str__(self):
        return '%s' % (self.nombre)  

class Control(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    operador = models.ManyToManyField(Funcionario)
    imagen = models.ImageField(upload_to='controles', null=True, blank=True)
    estado = models.ManyToManyField(Estado)
    accion = models.ManyToManyField(Accion)
    fecha = models.DateField()
    inicio = models.TimeField()
    fin = models.TimeField()
    observacion = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Controles"

    def __str__(self):
        return str(self.id)

