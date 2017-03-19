# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-19 13:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0003_mnitem_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(related_name='friend_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
