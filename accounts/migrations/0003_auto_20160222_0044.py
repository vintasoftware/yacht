# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_repos'),
    ]

    operations = [
        migrations.AddField(
            model_name='repos',
            name='parent_repo',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='repos',
            name='parent_repo_owner',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
