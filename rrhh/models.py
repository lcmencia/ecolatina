from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('avatar para tu perfil', upload_to='avatars', blank=True, null=True)
    ruc = models.CharField(unique=True,max_length=11,blank=True, null=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255,blank=True, null=True)
    telefono = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    direccion = models.CharField(max_length=255,blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id',)
 