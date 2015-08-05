# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HITtopic', '0007_comment_comment_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-pub_date']},
        ),
    ]
