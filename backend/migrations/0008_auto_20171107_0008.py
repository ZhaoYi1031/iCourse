# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20171107_0005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='code',
            new_name='course_code',
        ),
    ]
