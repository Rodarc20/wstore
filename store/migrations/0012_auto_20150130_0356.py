# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20150130_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='estado',
        ),
        migrations.AddField(
            model_name='carrito',
            name='status',
            field=models.CharField(default=b'open', max_length=6),
            preserve_default=True,
        ),
    ]
