# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20171122_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encargado',
            name='propiedad',
        ),
        migrations.AddField(
            model_name='encargado',
            name='propiedad',
            field=models.ManyToManyField(null=True, to='usuario.Propiedad', blank=True),
        ),
    ]
