# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-04 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='\u7528\u6237\u72b6\u6001'),
        ),
    ]
