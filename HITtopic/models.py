from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
	user=models.OneToOneField(User)
	email=models.EmailField()
	permission=models.IntegerField()
	def __str__(self):
		return self.user.username