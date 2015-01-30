# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_coment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('date', models.DateTimeField(verbose_name=b'date when generate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(default=1)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('carrito', models.ForeignKey(to='store.Carrito')),
                ('producto', models.ForeignKey(to='store.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('status', models.CharField(max_length=100)),
                ('voucher', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=300)),
                ('carrito', models.ForeignKey(to='store.Carrito')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='carrito',
            name='products',
            field=models.ManyToManyField(to='store.Product', through='store.Condition'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='carrito',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
