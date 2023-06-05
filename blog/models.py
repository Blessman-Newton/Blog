from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date



# Create your models here.

class Post(models.Model): 
	username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	headline = models.CharField(max_length=255, null=True, blank=False)
	body_text = models.TextField(max_length=10000, null=True, blank=False)
	pub_date = models.DateTimeField(default=datetime.now)
	mod_date = models.DateField(default=date.today)
	img = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=50)
 	#image = models.ImageField(upload_to='images', height_field=30%, width_field=70%, max_length=100%)
	number_of_comments = models.IntegerField(default=0)
  


	def __str__(self):
		return self.headline


    

   
    
    