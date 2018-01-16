# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-14 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filing', '0019_host_salt_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='salt_id',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='salt配置id'),
        ),
    ]