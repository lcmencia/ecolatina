# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20171122_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encargado',
            name='propiedad',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='encargado',
            field=models.ManyToManyField(to='usuario.Encargado'),
        ),
    ]
