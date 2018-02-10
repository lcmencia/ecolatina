from django.db import models
from usuario.models import *
import datetime
from django.contrib.auth.models import User


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

