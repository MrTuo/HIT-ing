# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HITtopic', '0005_auto_20150715_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('like_num', models.IntegerField(default=0)),
                ('dislike_num', models.IntegerField(default=0)),
                ('topic', models.ForeignKey(related_name='topics', to='HITtopic.Topic')),
                ('user', models.ForeignKey(related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
