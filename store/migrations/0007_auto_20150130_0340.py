# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20150130_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='status',
            field=models.CharField(max_length=7),
            preserve_default=True,
        ),
    ]
