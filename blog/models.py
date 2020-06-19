from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image

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

