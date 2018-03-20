# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-20 15:22
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('qq', models.IntegerField(null=True, unique=True, verbose_name='QQ')),
                ('email', models.CharField(max_length=200, null=True, unique=True, verbose_name='\u90ae\u4ef6')),
                ('user_icon', models.ImageField(default='image/default.png', max_length=500, upload_to='images/%Y/%m')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': '\u7528\u6237',
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todolist_text', models.TextField(max_length=200, verbose_name='\u4efb\u52a1\u5185\u5bb9')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4efb\u52a1\u53d1\u5e03\u65f6\u95f4')),
                ('todolist_state', models.IntegerField(verbose_name='\u4efb\u52a1\u72b6\u6001')),
                ('dodolist_flag', models.IntegerField(verbose_name='\u662f\u5426\u5220\u9664')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u5217\u8868',
                'verbose_name_plural': '\u4efb\u52a1\u5217\u8868',
            },
        ),
    ]
