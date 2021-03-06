# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('approved_date', models.DateTimeField(verbose_name='Approved Date')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(verbose_name='Created Date')),
                ('cardnumber', models.CharField(max_length=18)),
                ('customer_name', models.CharField(max_length=100)),
                ('billing_postal', models.CharField(max_length=5)),
                ('amount', models.IntegerField(default=0)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateway.Merchant')),
            ],
        ),
    ]
