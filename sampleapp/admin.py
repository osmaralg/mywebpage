from django.contrib import admin
from .models import Project, Author

# Register your models here.

admin.site.register(Author)
admin.site.register(Project)
