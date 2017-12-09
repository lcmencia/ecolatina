# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_auto_20171122_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='encargado',
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, blank=True, null=True),
        ),
    ]
