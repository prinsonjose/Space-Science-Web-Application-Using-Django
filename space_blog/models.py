from django.db import models

# Create your models here.

# Message sent from the contact form
class Contact(models.Model):
    name = models.CharField(max_length = 25)
    email = models.CharField(max_length = 25)
    subject = models.CharField(max_length = 100)
    message = models.TextField()
    contact_at = models.DateTimeField(auto_now_add=True)

# Project shown on the "Projects" page and in the home page slider
class Project(models.Model):
    project_title = models.CharField(max_length=100);
    project_image = models.ImageField(upload_to='project_img')
    project_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Blog post shown on the "Blog" page and the single post page
class Blogs(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_desc = models.TextField()
    blog_image = models.ImageField(upload_to = 'blog_img')
    created_at = models.DateTimeField(auto_now_add=True)
