# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-15 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('cashier', '0004_auto_20180315_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='user',
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='customer.Customer'),
        ),
    ]
