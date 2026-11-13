from django.urls import path
from . import views

app_name = 'login_page'

urlpatterns = [
    path('register', views.register, name='register'),   # create account
    path('login', views.login, name='login'),            # sign in with email + password
    path('logout', views.web_logout, name='logout')      # sign out
]
