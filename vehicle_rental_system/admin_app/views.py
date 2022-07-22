from django.shortcuts import render
from django.http import HttpResponse
from admin_app.forms import UserForm 
from admin_app.models import addBooking

# Create your views here.

def home(request):
    dict = {}
    return render(request, 'admin_app/index.html', context=dict)

def addAdmin(request):
    registered = False

    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
    else:
        user_form = UserForm()
    dict = {'user_form': user_form, 'registered':registered}
    return render(request, 'admin_app/add_admin.html', context=dict)

def addBooking(request):

    if request.method =='POST':
        type= request.POST.get('type')
        vehicleName= request.POST.get('vehicleName')
        capacity= request.POST.get('capacity')
        regNum= request.POST.get('regNum')
        cost= request.POST.get('cost')
        vehicleCondition= request.POST.get('vehicleCondition')
        bookingContact= request.POST.get('bookingContact')
        description= request.POST.get('description')

        add_booking = addBooking(type=type, vehicleName=vehicleName, capacity=capacity, regNum=regNum, cost=cost, vehicleCondition=vehicleCondition, bookingContact=bookingContact, description=description)
        add_booking.save()
    dict = {}
    return render(request, 'admin_app/add_booking.html', context=dict)

def adminView(request):
    dict = {}
    return render(request, 'admin_app/admin.html', context=dict)

def bookingReport(request):
    dict = {}
    return render(request, 'admin_app/booking_report.html', context=dict)

def changePassword(request):
    dict = {}
    return render(request, 'admin_app/change_password.html', context=dict)

def dashboard(request):
    dict = {}
    return render(request, 'admin_app/dashboard.html', context=dict)

def requisition(request):
    dict = {}
    return render(request, 'admin_app/requisition.html', context=dict)

def userView(request):
    dict = {}
    return render(request, 'admin_app/user.html', context=dict)

def logout(request):
    dict = {}
    return render(request, 'login_app/home.html', context=dict)

def profile(request):
    dict = {}
    return render(request, 'admin_app/profile.html', context=dict)