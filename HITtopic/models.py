# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    permission = models.IntegerField()
    topic_num = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username




class Topic(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    like_num = models.IntegerField(default=0)
    dislike_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='users')
    topic = models.ForeignKey(Topic, related_name='topics')
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    like_num = models.IntegerField(default=0)
    dislike_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    def __unicode__(self):
        return self.topic.title + "--by:" + self.user.username

    class Meta:
        ordering = ['-pub_date']
