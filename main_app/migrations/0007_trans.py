# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20170114_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('submitted', models.DateTimeField()),
                ('processed', models.DateTimeField()),
            ],
        ),
    ]
