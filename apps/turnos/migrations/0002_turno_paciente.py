# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-26 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0009_paciente_empleado'),
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente'),
        ),
    ]
