# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='coment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coment', models.CharField(max_length=1000)),
                ('rank', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name=b'date when comented')),
                ('product', models.ForeignKey(to='store.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
