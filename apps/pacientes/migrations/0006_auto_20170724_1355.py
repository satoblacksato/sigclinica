# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-24 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20170725_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='tipo_telefono',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]