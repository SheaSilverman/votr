# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-08-09 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180809_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='county',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='voter',
            name='dob',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='voter',
            name='gender',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='voter',
            name='party',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='voter',
            name='race',
            field=models.CharField(max_length=200),
        ),
    ]
