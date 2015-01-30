# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_carrito_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='status',
            field=models.CharField(default=b'open', max_length=10),
            preserve_default=True,
        ),
    ]
