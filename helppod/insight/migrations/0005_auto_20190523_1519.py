# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-23 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0004_task_service_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='service_time',
            field=models.DateTimeField(),
        ),
    ]
