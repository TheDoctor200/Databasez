# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deposito', '0006_campione_bar'),
    ]

    operations = [
        migrations.AddField(
            model_name='campione',
            name='valore2',
            field=models.CharField(default=0, max_length=10, verbose_name='Corrente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campione',
            name='valore3',
            field=models.CharField(default=0, max_length=10, verbose_name='Potenza'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campione',
            name='valore',
            field=models.CharField(max_length=10, verbose_name='Tensione'),
        ),
    ]
