# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HITtopic', '0004_myuser_avatar_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='avatar_name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(default=b'avatar/default.JPG', upload_to=b''),
        ),
    ]
