# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-26 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0003_turno_motivo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turno',
            options={},
        ),
        migrations.AlterField(
            model_name='turno',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turno',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
