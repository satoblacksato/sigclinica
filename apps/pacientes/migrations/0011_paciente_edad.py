# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-18 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0010_auto_20170918_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.DateField(blank=True, null=True),
        ),
    ]
