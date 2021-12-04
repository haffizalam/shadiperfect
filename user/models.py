from django.db import models
from django.contrib.auth.models import User
from perfectshadi.models import UserProfile
# Create your models here.

class UserData(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	pic=models.ImageField(upload_to="product_image",blank=True)
	faname=models.CharField(max_length=50)
	mname=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	mstatus=models.CharField(max_length=20)
	height=models.CharField(max_length=10)
	profession=models.CharField(max_length=50)
	qualification=models.CharField(max_length=50)
	religion=models.CharField(max_length=50)
	mothertongue=models.CharField(max_length=50)
	cityname=models.CharField(max_length=50)
	dist=models.CharField(max_length=50)
	pin=models.CharField(max_length=10)
	hobbies=models.CharField(max_length=100)

	