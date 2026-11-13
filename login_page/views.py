
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils.http import url_has_allowed_host_and_scheme


# Create a new account from the registration form
def register(request):

    if request.method == "POST":

        # Read the values typed in the form (names match the inputs in registration.html)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_password')
        username = request.POST.get('username')

        # Check password
        if password != confirm_pass:
            messages.error(request, "Confirm password does not match")
            return redirect('/auth/register')

        # Check existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('/auth/register')

        # Check existing username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/auth/register')

        # Create user (create_user hashes the password)
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )

        messages.success(request, "Registration successful")
        return redirect('/auth/login')

    return render(request, 'registration.html')


# Sign in using email + password (the email is converted to the username Django expects)
def login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Find the account that belongs to this email
            user_obj = User.objects.get(email=email)

            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user is not None:
                auth_login(request, user)
                # Return to the protected page the visitor tried to open (e.g. a blog post).
                # url_has_allowed_host_and_scheme blocks redirects to other websites.
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    return redirect(next_url)
                return redirect('space_blog:home')

            else:
                messages.error(request, "Incorrect password")

        except User.DoesNotExist:
            messages.error(request, "Email does not exist")

    return render(request, 'login.html')

# Sign out and go back to the home page
def web_logout(request):
    logout(request)
    return redirect('space_blog:home')
