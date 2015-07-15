# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HITtopic', '0004_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
