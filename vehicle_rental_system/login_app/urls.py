from urllib.parse import urlparse
from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login, name='user_login'),
    path('admin_login/',views.admin_login, name='admin_login'),


]