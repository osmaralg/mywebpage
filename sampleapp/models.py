from django.db import models

# Create your models here.
class Project(models.Model):
    author = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'static/img/', default = 'static/field.jpg')


class Author(models.Model):
	name = models.CharField(max_length=42)
	last_name = models.CharField(max_length=42)
	created_on = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to = 'static/img/', default = 'static/field.jpg')