# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-30 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190829_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=60),
        ),
    ]
