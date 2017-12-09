# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Acciones',
            },
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('imagen', models.ImageField(upload_to='controles', blank=True, null=True)),
                ('fecha', models.DateField()),
                ('inicio', models.TimeField()),
                ('fin', models.TimeField()),
                ('observacion', models.TextField(blank=True, null=True)),
                ('accion', models.ManyToManyField(to='roedores.Accion')),
            ],
            options={
                'verbose_name_plural': 'Controles',
            },
        ),
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('propiedad', models.IntegerField(editable=False)),
                ('cliente', models.IntegerField(editable=False)),
                ('usuario', models.IntegerField(editable=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('instalador', models.ManyToManyField(to='usuario.Funcionario')),
                ('sector', models.ForeignKey(to='usuario.Sector')),
            ],
            options={
                'verbose_name_plural': 'Estaciones',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.AddField(
            model_name='control',
            name='estacion',
            field=models.ForeignKey(to='roedores.Estacion'),
        ),
        migrations.AddField(
            model_name='control',
            name='estado',
            field=models.ManyToManyField(to='roedores.Estado'),
        ),
        migrations.AddField(
            model_name='control',
            name='operador',
            field=models.ManyToManyField(to='usuario.Funcionario'),
        ),
    ]
