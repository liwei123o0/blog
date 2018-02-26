# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_content', models.TextField(verbose_name='\u535a\u5ba2\u5185\u5bb9')),
                ('blog_title', models.CharField(max_length=200, verbose_name='\u535a\u5ba2\u6807\u9898')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u535a\u5ba2\u521b\u5efa\u65f6\u95f4')),
                ('modified_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u535a\u5ba2\u4fee\u6539\u65f6\u95f4')),
                ('excerpt', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['-created_time'],
                'verbose_name': '\u535a\u5ba2\u4fe1\u606f',
                'verbose_name_plural': '\u535a\u5ba2\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_name', models.CharField(max_length=20, verbose_name='\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
    ]
