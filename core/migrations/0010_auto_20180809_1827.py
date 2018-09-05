# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-08-09 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180807_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='congress',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='county_commission',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='precinct',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='school_board',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='state_house',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='state_senate',
            field=models.IntegerField(default=0, null=True),
        ),
    ]