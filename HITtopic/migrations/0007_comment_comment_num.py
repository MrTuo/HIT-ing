# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HITtopic', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_num',
            field=models.IntegerField(default=0),
        ),
    ]
