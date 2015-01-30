# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20150130_0340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='status',
        ),
    ]
