# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-17 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mnlist',
            name='name',
            field=models.CharField(default='hej', max_length=200),
            preserve_default=False,
        ),
    ]