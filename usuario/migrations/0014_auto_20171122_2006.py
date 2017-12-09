# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_remove_propiedad_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
