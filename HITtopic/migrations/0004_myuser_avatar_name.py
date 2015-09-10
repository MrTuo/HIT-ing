# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HITtopic', '0003_auto_20150907_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='avatar_name',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
