from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

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


