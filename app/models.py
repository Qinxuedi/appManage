from django.db import models

# Create your models here.

class Software(models.Model):
	called=models.CharField(max_length=30)
	softname=models.CharField(max_length=30)
	download_times=models.IntegerField(max_length=10000)
	#url=models.URLField()

class User(models.Model):
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	softwares=models.ManyToManyField(Software)

class Comment(models.Model):
	user=models.ForeignKey(User)
	soft=models.ForeignKey(Software)
	star=models.IntegerField(max_length=5)
	comment=models.CharField(max_length=200)



