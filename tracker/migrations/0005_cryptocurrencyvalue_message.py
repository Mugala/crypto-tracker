# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_cryptocurrencyvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrencyvalue',
            name='message',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
