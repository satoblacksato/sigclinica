# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20170725_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
