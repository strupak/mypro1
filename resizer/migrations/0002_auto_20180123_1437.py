# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='images/'),
        ),
    ]