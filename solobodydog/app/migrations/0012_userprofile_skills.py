# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150822_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.CharField(max_length=30), size=None),
            preserve_default=False,
        ),
    ]
