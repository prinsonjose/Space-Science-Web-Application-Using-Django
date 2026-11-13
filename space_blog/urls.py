from django.urls import path
from . import views

app_name = 'space_blog'

urlpatterns = [
    path('', views.home, name='home'),                       # home page
    path('about-us', views.about_us, name='about_us'),       # about page
    path('project', views.projects, name='projects'),        # all projects
    path('blog', views.blog, name='blog'),                   # all blog posts
    path('contact', views.contact, name='contact'),          # contact form
    path('post/<int:id>/', views.post, name='post'),         # single blog post
    path('projectlist/<int:id>/', views.projectlist, name='projectlist')  # single project
]
