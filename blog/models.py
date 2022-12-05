from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



# Create your models here.
class Post(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
	title = models.CharField(max_length=100, null=False, blank=False)
	body = models.TextField(max_length=100000, null=False, blank=False)
	date_posted = models.DateTimeField(default=datetime.now)
	img = models.ImageField(null=False,  blank=False)


	def __str__(self):
		return self.title