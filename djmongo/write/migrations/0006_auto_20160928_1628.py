# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-28 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0005_auto_20160113_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeapiip',
            name='from_ip',
            field=models.TextField(default=b'127.0.0.1', help_text='Only accept requests from a IP in this list separated by whitespace . 0.0.0.0 means all.', max_length=2048, verbose_name='From IPs'),
        ),
    ]
