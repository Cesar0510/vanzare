# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-27 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20171031_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='producto_base',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='recibido',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='ProductoBase',
        ),
    ]
