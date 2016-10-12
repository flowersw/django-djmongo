# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-28 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=256)),
                ('collection_name', models.CharField(max_length=256)),
                ('search_keys', models.TextField(blank=True, default=b'', help_text=b'The default, blank, returns\n                                                all keys. Providing a list of\n                                                keys, separated by whitespace,\n                                                limits the API search to only\n                                                these keys.', max_length=4096)),
            ],
            options={
                'verbose_name': 'Search API using No Auth (Public)',
                'verbose_name_plural': 'Search APIs using No Auth (Public)',
            },
        ),
        migrations.AlterModelOptions(
            name='databaseaccesscontrol',
            options={'verbose_name': 'Search API using HTTPAuth', 'verbose_name_plural': 'Search APIs using HTTPAuth'},
        ),
        migrations.AlterField(
            model_name='databaseaccesscontrol',
            name='search_keys',
            field=models.TextField(blank=True, default=b'', help_text=b'The default, blank, returns\n                                                all keys. Providing a list of\n                                                keys, separated by whitespace,\n                                                limits the API search to only\n                                                these keys.', max_length=4096),
        ),
        migrations.AlterField(
            model_name='savedsearch',
            name='return_keys',
            field=models.TextField(blank=True, default=b'', help_text='Default is blank which returns all keys. Separate keys by white space to limitthe keys that are returned.', max_length=2048),
        ),
        migrations.AlterField(
            model_name='savedsearch',
            name='type_mapper',
            field=models.TextField(default=b'{}', max_length=2048, verbose_name='Map non-string variables to numbers or Boolean'),
        ),
        migrations.AlterUniqueTogether(
            name='publicreadapi',
            unique_together=set([('database_name', 'collection_name')]),
        ),
    ]