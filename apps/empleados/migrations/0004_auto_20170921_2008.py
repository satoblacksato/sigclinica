# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-21 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_empleado_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='categoria',
            field=models.CharField(blank=True, choices=[('medico', 'Médico'), ('secretariado', 'Secretariado'), ('programador', 'Programador')], max_length=800, null=True),
        ),
    ]
