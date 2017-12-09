# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_auto_20171122_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ruc',
            field=models.CharField(max_length=11, blank=True, null=True),
        ),
    ]
