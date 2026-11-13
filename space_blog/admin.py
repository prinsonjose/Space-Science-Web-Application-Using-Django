from django.contrib import admin
from .models import Contact, Project, Blogs
# Register your models here.

# Make the models editable from the /admin/ site
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Blogs)
