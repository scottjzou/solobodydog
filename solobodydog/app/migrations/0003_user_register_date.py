# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(default=None),
        ),
    ]
