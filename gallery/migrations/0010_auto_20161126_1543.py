# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_photograph_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='copyright',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='photograph',
            name='credit',
            field=models.TextField(blank=True),
        ),
    ]