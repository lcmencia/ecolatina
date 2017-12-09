# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_auto_20171122_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(null=True, max_length=255, unique=True, blank=True),
        ),
    ]
