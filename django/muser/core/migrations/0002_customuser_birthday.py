# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 08:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
