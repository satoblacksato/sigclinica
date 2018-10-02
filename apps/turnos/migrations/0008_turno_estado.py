# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-22 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0007_auto_20170922_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='estado',
            field=models.CharField(blank=True, choices=[('presente', 'presente'), ('cambio', 'cambio'), ('atendido', 'atendido')], max_length=800, null=True),
        ),
    ]
