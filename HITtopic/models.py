from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
	user=models.OneToOneField(User)
	email=models.EmailField()
	permission=models.IntegerField()
	def __str__(self):
		return self.user.username

class Topic(models.Model):
	author=models.ForeignKey(User)
	title=models.CharField(max_length=150)
	pub_date=models.DateTimeField(auto_now=True)
	content=models.TextField()
	like_num=models.IntegerField(default=0)
	dislike_num=models.IntegerField(default=0)
	comment_num=models.IntegerField(default=0)
	def __str__(self):
		return self.title