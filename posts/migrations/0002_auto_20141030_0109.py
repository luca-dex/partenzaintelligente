# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_last_edit',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 30, 1, 9, 18, 848292), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 30, 1, 9, 18, 848217), auto_now_add=True),
            preserve_default=True,
        ),
    ]
