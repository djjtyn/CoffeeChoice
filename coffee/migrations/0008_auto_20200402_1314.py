# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-02 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0007_auto_20200327_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Coffee',
            new_name='coffee',
        ),
    ]
