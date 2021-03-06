# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-26 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=800, null=True)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('allDay', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Turnos',
                'verbose_name': 'Turno',
            },
        ),
    ]
