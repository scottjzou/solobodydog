# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150822_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
