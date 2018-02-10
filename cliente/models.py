from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from rrhh.models import *
import datetime

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    avatar = models.ImageField('avatar para tu perfil', upload_to='avatars', blank=True, null=True)
    ruc = models.CharField(max_length=11,blank=True, null=True)
    razon_social = models.CharField(unique=True,max_length=255,blank=True, null=True)
    telefono = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.razon_social

    class Meta:
        ordering = ('id',)

class Encargado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255,blank=True, null=True)
    telefono = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)

class Propiedad(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField('Imagen del lugar', upload_to='property', blank=True, null=True)
    direccion = models.CharField(max_length=255,blank=True, null=True)
    ciudad = models.CharField(max_length=255,blank=True, null=True)
    location = PlainLocationField(based_fields=['ciudad'], default='-25.296223240855703,-57.63144493103027', zoom=7,blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Propiedades"

    def __str__(self):
        return self.nombre

    

class Sector(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField('Imagen del sector', upload_to='sector', blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Sectores"

    def __str__(self):
        return '%s' % (self.nombre)


class Estacion(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True)
    instalador = models.ManyToManyField(Funcionario)
    
    class Meta:
        verbose_name_plural = "Estaciones"

    def __str__(self):
        return str(self.id)

    


class Control(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    operador = models.ManyToManyField(Funcionario)
    imagen = models.ImageField(upload_to='controles', null=True, blank=True)
    e_ausencia = models.BooleanField(default=False,verbose_name='Ausencia de cebo')
    e_buen_estado = models.BooleanField(default=False,verbose_name='Cebo en buen estado')
    e_consumido = models.BooleanField(default=False,verbose_name='Cebo consumido')
    e_deteriorado = models.BooleanField(default=False,verbose_name='Cebo deteriorado')
    e_capturado = models.BooleanField(default=False,verbose_name='Captura muerta')
    e_pa_deteriorada = models.BooleanField(default=False,verbose_name='Placa deteriorada')
    e_pa_buen_estado = models.BooleanField(default=False,verbose_name='Placa en buen estado')
    e_no_acceso = models.BooleanField(default=False,verbose_name='No se pudo acceder')
    a_reposicion = models.BooleanField(default=False,verbose_name='Reposicion')
    a_limpieza = models.BooleanField(default=False,verbose_name='Limpieza')
    a_reemplazo = models.BooleanField(default=False,verbose_name='Reemplazo')
    fecha = models.DateField()
    inicio = models.TimeField()
    fin = models.TimeField()
    observacion = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Controles"

    def __str__(self):
        return str(self.id)



