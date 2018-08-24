# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-08-05 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180805_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoterException',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=200)),
                ('voterID', models.IntegerField(default=0, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
