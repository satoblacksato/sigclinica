# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-16 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('complementos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=600, null=True)),
                ('apellido', models.CharField(blank=True, max_length=600, null=True)),
                ('documento', models.CharField(blank=True, max_length=600, null=True)),
                ('tipo_documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='complementos.TipoDocumento')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
