from .models import Contact, Project, Blogs
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# Projects / blogs used by the header drop-down menu.
# Every page extends the same menu, so every view passes these two extra values.
def nav_links():
    return {'nav_projects': Project.objects.all(), 'nav_blogs': Blogs.objects.all()}

def home(request):
    project = Project.objects.all()
    blog = Blogs.objects.all()
    # FIX: "featured projects" were read from Blogs (which has no project_image), so no image was shown
    project2 = Project.objects.order_by('-created_at')[:4]
    blog2 = Blogs.objects.order_by('-created_at')[:2]
    return render(request, 'index.html', {'projects':project, 'blogs':blog, 'blogs2' : blog2, 'project2':project2, **nav_links()})

def about_us(request):
    return render(request, 'about.html', nav_links())

def projects(request):
    project = Project.objects.all()
    return render(request, 'projects.html', {'projects':project, **nav_links()})

def blog(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog.html', {'blogs':blogs, **nav_links()})

def contact(request):
    if request.method == 'POST':
        # FIX: every field was read from the "Name" input, so name/email/subject/message all saved the same value
        name_input = request.POST.get('Name')
        email_input = request.POST.get('Email')
        subject_input = request.POST.get('Subject')
        message_input = request.POST.get('message')

        user = Contact(
            name = name_input,
            email = email_input,
            subject = subject_input,
            message = message_input
        )

        user.save()
        print(name_input, email_input, subject_input, message_input)
        # Show a confirmation and redirect, so refreshing the page does not send the form twice
        messages.success(request, "Thank you! Your message has been sent.")
        return redirect('space_blog:contact')
    return render(request, 'contact.html', nav_links())

# FIX: only logged-in users can read a full post. Before, "Read More" asked for login
# but the image link (and typing /post/1/) opened the post without any login.
@login_required
def post(request, id):
    # FIX: an unknown id raised a 500 error (DoesNotExist) - now it returns a normal 404 page
    blog = get_object_or_404(Blogs, id=id)
    blog2 = Blogs.objects.order_by('-created_at')[:2]
    return render(request, 'singlepost.html', {'blogs':blog, 'blogs2':blog2, **nav_links()})

# FIX: same rule for a single project page
@login_required
def projectlist(request, id):
    # FIX: same as above - 404 instead of 500 for an unknown project id
    project = get_object_or_404(Project, id=id)
    print(project)
    return render(request, 'proj1.html', {'projects':project, **nav_links()})
