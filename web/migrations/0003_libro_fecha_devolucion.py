# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_libro_prestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha_devolucion',
            field=models.DateTimeField(null=True),
        ),
    ]
