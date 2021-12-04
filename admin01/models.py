from django.db import models

# Create your models here.


class religion(models.Model):
	religioame=models.CharField(max_length=50)
class city(models.Model):
	cityname=models.CharField(max_length=50)
class lang(models.Model):
	mothertongue=models.CharField(max_length=50)
class story(models.Model):
	img=models.ImageField(upload_to="product_image",blank=True)
	bride=models.CharField(max_length=20)
	bridegroom=models.CharField(max_length=20)
	story=models.CharField(max_length=200)
