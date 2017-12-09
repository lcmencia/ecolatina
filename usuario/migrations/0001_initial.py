# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='avatar para tu perfil', blank=True, null=True)),
                ('ruc', models.CharField(max_length=11, blank=True, null=True, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('razon_social', models.CharField(max_length=255, blank=True, null=True)),
                ('telefono', models.CharField(max_length=15, blank=True, null=True)),
                ('email', models.EmailField(max_length=255, blank=True, null=True)),
                ('direccion', models.CharField(max_length=255, blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='avatar para tu perfil', blank=True, null=True)),
                ('ruc', models.CharField(max_length=11, blank=True, null=True, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('razon_social', models.CharField(max_length=255, blank=True, null=True)),
                ('telefono', models.CharField(max_length=15, blank=True, null=True)),
                ('email', models.EmailField(max_length=255, blank=True, null=True)),
                ('direccion', models.CharField(max_length=255, blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('usuario', models.IntegerField(editable=False)),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to='property', verbose_name='Imagen del lugar', blank=True, null=True)),
                ('direccion', models.CharField(max_length=255, blank=True, null=True)),
                ('ciudad', models.CharField(max_length=255, blank=True, null=True)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(to='usuario.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Propiedades',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('imagen', models.ImageField(upload_to='sector', verbose_name='Imagen del sector', blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('propiedad', models.ForeignKey(to='usuario.Propiedad')),
            ],
            options={
                'verbose_name_plural': 'Sectores',
            },
        ),
    ]
