# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-10 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaclinicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaclinica',
            name='tratamiento',
            field=models.TextField(blank=True, max_length=9200, null=True),
        ),
    ]
