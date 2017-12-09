# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-07 12:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20171124_0212'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('qty', models.IntegerField()),
                ('total', models.FloatField(blank=True, default=None)),
                ('invoice_number', models.CharField(blank=True, max_length=128)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('subtotal', models.FloatField(blank=True, default=None)),
                ('product_warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductWarehouse')),
                ('received_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='received_product.ReceivedProduct')),
            ],
        ),
    ]