# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=30), blank=True),
        ),
    ]
