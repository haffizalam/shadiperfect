from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	dob=models.DateTimeField(max_length=8)
	usertype=models.CharField(max_length=20,default='user')
	mobile=models.CharField(max_length=20)
class Contact(models.Model):
	name=models.CharField(max_length=8)
	email=models.CharField(max_length=20)
	text=models.CharField(max_length=100)