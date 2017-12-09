# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255, blank=True, null=True)),
                ('telefono', models.CharField(max_length=15, blank=True, null=True)),
                ('email', models.EmailField(max_length=255, blank=True, null=True)),
                ('direccion', models.CharField(max_length=255, blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
