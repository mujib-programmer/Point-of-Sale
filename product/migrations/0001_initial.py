# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 04:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merk', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200)),
                ('size', models.CharField(choices=[('40x30', '40x30'), ('30x40', '30x40'), ('60x60', '60x60')], max_length=10)),
                ('color', models.CharField(max_length=15)),
                ('price', models.FloatField()),
                ('merk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='merk.Merk')),
            ],
        ),
        migrations.CreateModel(
            name='ProductWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='product.Product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='warehouse.Warehouse')),
            ],
        ),
    ]
