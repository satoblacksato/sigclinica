# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-25 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_auto_20170724_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='observacion',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]