# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20150129_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='status',
            field=models.CharField(default='open', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 30, 3, 36, 8, 984046, tzinfo=utc), verbose_name=b'date when generate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrito',
            name='total_price',
            field=models.DecimalField(default=0, max_digits=9, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(default=0, max_digits=9, decimal_places=2),
            preserve_default=True,
        ),
    ]
