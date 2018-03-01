# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 19:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(help_text='User assigned to this profile.', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('description', models.CharField(blank=True, help_text='Put your profile description', max_length=255, null=True, verbose_name='Description')),
                ('avatar', models.ImageField(blank=True, help_text='Your account image', null=True, upload_to='', verbose_name='Image')),
            ],
        ),
    ]
