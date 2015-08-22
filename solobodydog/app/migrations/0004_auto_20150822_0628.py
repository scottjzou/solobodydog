# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=models.DateTimeField(),
        ),
    ]
