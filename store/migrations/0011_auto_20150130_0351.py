# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20150130_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='status',
        ),
        migrations.AddField(
            model_name='carrito',
            name='estado',
            field=models.CharField(default=b'open', max_length=10),
            preserve_default=True,
        ),
    ]
