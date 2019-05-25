# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-23 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0006_auto_20190523_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='drop',
            new_name='drop_location',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='pickup',
            new_name='pickup_location',
        ),
        migrations.AddField(
            model_name='task',
            name='phone',
            field=models.CharField(default=984203, max_length=10),
            preserve_default=False,
        ),
    ]
