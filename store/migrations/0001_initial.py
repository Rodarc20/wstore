# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('spec', models.CharField(max_length=1000)),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('special_price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('rank', models.IntegerField(default=0)),
                ('stock', models.CharField(max_length=30)),
                ('product_type', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('date', models.DateTimeField(verbose_name=b'date when generate')),
                ('status', models.CharField(max_length=100)),
                ('voucher', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=300)),
                ('products', models.ManyToManyField(to='store.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
