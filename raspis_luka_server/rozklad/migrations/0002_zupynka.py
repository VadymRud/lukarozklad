# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rozklad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zupynka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('place', models.FloatField(verbose_name='Place by serial number')),
            ],
            options={
                'verbose_name': 'Zupynka Name',
                'verbose_name_plural': 'Zupynka Names',
                'ordering': ['name'],
            },
        ),
    ]
