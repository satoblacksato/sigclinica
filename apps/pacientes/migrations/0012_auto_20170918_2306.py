# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-18 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0011_paciente_edad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='edad',
            new_name='fecha_nacimiento',
        ),
    ]