# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Deposito', '0003_campione_frah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campione',
            old_name='frah',
            new_name='codice',
        ),
    ]
