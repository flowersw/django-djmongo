# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-12 18:22
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(choices=[(b'db-all', b'All MongoDB'), (b'db-write', b'Write MongoDB'), (b'db-read', b'Read MongoDB'), (b'create-other-users', b'create-other-users'), (b'create-any-socialgraph', b'create-any-socialgraph'), (b'delete-any-socialgraph', b'delete-any-socialgraph')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(default=datetime.date.today)),
                ('grantee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grantee', to=settings.AUTH_USER_MODEL)),
                ('grantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grantor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
                'get_latest_by': 'created_on',
            },
        ),
        migrations.AlterUniqueTogether(
            name='socialgraph',
            unique_together=set([('grantor', 'grantee')]),
        ),
        migrations.AlterUniqueTogether(
            name='permission',
            unique_together=set([('user', 'permission_name')]),
        ),
    ]
