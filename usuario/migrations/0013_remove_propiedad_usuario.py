# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_auto_20171122_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='usuario',
        ),
    ]
