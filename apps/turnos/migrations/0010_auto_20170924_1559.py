# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-24 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0009_turno_backgroundcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='backgroundColor',
            field=models.CharField(blank=True, default='#80FF00', max_length=2000, null=True),
        ),
    ]