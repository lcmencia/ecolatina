# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_encargado'),
    ]

    operations = [
        migrations.AddField(
            model_name='encargado',
            name='cliente',
            field=models.ForeignKey(default=1, to='usuario.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encargado',
            name='propiedad',
            field=models.ForeignKey(null=True, blank=True, to='usuario.Propiedad'),
        ),
    ]
