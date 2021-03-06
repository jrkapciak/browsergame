# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 20:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text="Character's nickname", max_length=30, verbose_name='Nickname')),
                ('level', models.PositiveSmallIntegerField(default=1, help_text="Character's actual level", validators=[django.core.validators.MinValueValidator(1)], verbose_name='Level')),
                ('experience_points', models.IntegerField(default=1, help_text='Actual experience points', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Experience points')),
                ('health', models.PositiveSmallIntegerField(default=100, help_text="Actuacl character'health value", validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Health')),
                ('action_points', models.PositiveSmallIntegerField(default=1000, help_text='Avaiable points to be used in mission etc.', validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)], verbose_name='Action points')),
                ('ruby_number', models.PositiveSmallIntegerField(default=0, help_text='Number of avaiable rubies', validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)], verbose_name='Ruby number')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='parameters',
            field=models.OneToOneField(help_text="Character's parameters", on_delete=django.db.models.deletion.CASCADE, to='character.Parameters', verbose_name='Parameters'),
        ),
    ]
