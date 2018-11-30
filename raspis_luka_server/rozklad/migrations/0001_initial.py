# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('type', models.CharField(max_length=200, verbose_name='Type Vehicle')),
            ],
            options={
                'verbose_name': 'Transport Name',
                'verbose_name_plural': 'Transport Names',
                'ordering': ['name'],
            },
        ),
    ]