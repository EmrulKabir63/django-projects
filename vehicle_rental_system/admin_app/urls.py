from urllib.parse import urlparse
from django.urls import path
from admin_app import views

app_name = 'admin_app'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('addAdmin/',views.addAdmin, name='addAdmin'),
    path('addBooking/',views.addBooking, name='addBooking'),
    path('adminView/',views.adminView, name='adminView'),
    path('bookingReport/',views.bookingReport, name='bookingReport'),
    path('changePassword/',views.changePassword, name='changePassword'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('requisition/',views.requisition, name='requisition'),
    path('userView/',views.userView, name='userView'),
    path('profile/',views.profile, name='profile'),


]