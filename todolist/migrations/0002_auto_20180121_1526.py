# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('qq', models.IntegerField(null=True, verbose_name='QQ')),
                ('email', models.CharField(max_length=200, null=True, verbose_name='\u90ae\u4ef6')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': '\u4efb\u52a1\u5217\u8868', 'verbose_name_plural': '\u4efb\u52a1\u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='todolist',
            name='dodolist_flag',
            field=models.IntegerField(verbose_name='\u662f\u5426\u5220\u9664'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='pub_date',
            field=models.DateTimeField(verbose_name='\u4efb\u52a1\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='todolist_state',
            field=models.IntegerField(verbose_name='\u4efb\u52a1\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='todolist_text',
            field=models.CharField(max_length=200, verbose_name='\u4efb\u52a1\u5185\u5bb9'),
        ),
    ]
