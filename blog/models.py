from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image
from django_mysql.models import ListCharField

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	summary = models.TextField(default="")
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	image = models.ImageField(upload_to='media/', null=True, blank=True, height_field="height_field", width_field="width_field");
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class CV(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	email = models.EmailField(max_length=254, default='')
	website = models.URLField(max_length=200,  null=True, blank=True)
	number = models.CharField(max_length=11, default='', blank=True)
	headshot = models.ImageField(upload_to='media/', null=True, blank=True)
	personal_profile = models.TextField(default='')
	skills = ListCharField(base_field=models.CharField(max_length=100), size=10, max_length=(10*101), default=[])

	def publish(self):
		self.save()

	def __str__(self):
		return self.name


class WorkExperience(models.Model):
	title = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	duration = models.CharField(max_length=200)
	description = models.TextField(default='')

	def publish(self):
		self.save()

	def __str__(self):
		return self.title


class Education(models.Model):
	institution = models.CharField(max_length=300)
	qualification = models.CharField(max_length=400, blank=True, default=' ')
	duration = models.CharField(max_length=200)
	description = models.TextField(default='')

	def publish(self):
		self.save()

	def __str__(self):
		return self.institution


class Activity(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(default='')

	def publish(self):
		self.save()

	def __str__(self):
		return self.title


class Calligraphy(models.Model):
	description = models.TextField(default='')
	image = models.ImageField(upload_to='media/calligraphy/', null=True, blank=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.description


class Photography(models.Model):
	description = models.TextField(default='')
	image = models.ImageField(upload_to='media/photography/', null=True, blank=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.description