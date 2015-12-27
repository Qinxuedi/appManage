from django.db import models

# Create your models here.

class recommend_app(models.Model):
	pic_url=models.CharField(max_length=40)
	show=models.CharField(max_length=10)
	url=models.CharField(max_length=100)
	name=models.CharField(max_length=30)
	position=models.IntegerField()
	#url=models.URLField()

class rank_app(models.Model):
	pic_url=models.CharField(max_length=40)
	name=models.CharField(max_length=30)
	url=models.CharField(max_length=100)
	star=models.IntegerField()
	rank=models.IntegerField()
	download=models.CharField(max_length=40)
	
<<<<<<< HEAD
	

'''class User(models.Model):
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	softwares=models.ManyToManyField(Software)

=======
class Software(models.Model):
	name=models.CharField(max_length=255)
	img=models.CharField(max_length=255)
	version=models.CharField(max_length=255)
	size=models.CharField(max_length=255)

class Favor(models.Model):
	favor = models.DateField()
'''
class User(models.Model):
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	software=models.ManyToManyField(Software)
	favor=models.ManyToManyField(Favor)
'''
'''
>>>>>>> G
class Comment(models.Model):
	user=models.ForeignKey(User)
	soft=models.ForeignKey(Software)
	star=models.IntegerField(max_length=5)
<<<<<<< HEAD
	comment=models.CharField(max_length=200)'''

=======
	comment=models.CharField(max_length=200)
'''
>>>>>>> G


