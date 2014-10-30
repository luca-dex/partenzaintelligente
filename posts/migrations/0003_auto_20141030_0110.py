# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20141030_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_last_edit',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
        ),
    ]
