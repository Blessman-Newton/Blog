from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date



# Create your models here.

class Post(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
	headline = models.CharField(max_length=255, null=True, blank=False)
	body_text = models.TextField(max_length=100, null=True, blank=False)
	pub_date = models.DateTimeField(default=datetime.now, blank=True)
	mod_date = models.DateField(default=date.today)
	img = models.ImageField(null=False,  blank=False)
	number_of_comments = models.IntegerField(default=0)
 


	def __str__(self):
		return self.headline

    

   
    
    