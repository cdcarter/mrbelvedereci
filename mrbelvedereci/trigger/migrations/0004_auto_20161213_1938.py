# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trigger', '0003_auto_20161128_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trigger',
            name='build_pr_commits',
        ),
        migrations.AlterField(
            model_name='trigger',
            name='type',
            field=models.CharField(choices=[('manual', 'Manual'), ('commit', 'Commit'), ('tag', 'Tag')], max_length=8),
        ),
    ]
