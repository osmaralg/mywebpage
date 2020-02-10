from django.db import models

# Create your models here.
class Project(models.Model):
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=42, default='No title')
    url = models.CharField(max_length=42, null=True, blank=True)
    content = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=42)
    last_name = models.CharField(max_length=42)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
    email = models.EmailField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.last_name

class Category(models.Model):
    name = models.CharField(max_length=42)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=42)

    def __str__(self):
        return self.name
        

