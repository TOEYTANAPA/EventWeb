from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
	"""docstring for Person"""
	name=models.CharField(max_length=100)
	def __unicode__(self):
		return u"%s"%(self.name)

class Image(models.Model):
	"""docstring for Image"""
	image=models.ImageField(upload_to='images')
	description=models.CharField(max_length=100,blank=True,null=True)


# class User(models.Model):
#     # This field is required.
#     user = models.CharField(max_length=18)
#     # Other fields here
#     # accepted_eula = models.BooleanField()
#     # favorite_animal = models.CharField(max_length=20, default="Dragons.")
