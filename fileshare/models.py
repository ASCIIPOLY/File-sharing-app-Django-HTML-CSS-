from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	files = models.FileField(null=True,blank=True,upload_to='Files')
	content = models.TextField(max_length=200)
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.files.name)
		extension = extension.lower()
		return extension
