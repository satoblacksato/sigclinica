# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-22 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0006_auto_20170922_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='fecha',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='turno',
            name='hora',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
