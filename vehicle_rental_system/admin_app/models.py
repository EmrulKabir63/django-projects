from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class addBooking(models.Model):
    vehicle_type_choices =[
        ('car','car'),
        ('micro','micro'),
        ('bike','bike'),
        ('pickup','pickup'),
        ('miniBus','miniBus'),
        ('bus','bus'),
    ]
    vehicleCondition_choices =[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]
    type = models.CharField(max_length=10, choices=vehicle_type_choices, default='car')
    vehicleName = models.CharField(max_length=50)
    capacity = models.IntegerField()
    regNum = models.IntegerField()
    cost = models.IntegerField()
    vehicleCondition = models.CharField(max_length=5, choices=vehicleCondition_choices, default='3')
    bookingContact = models.IntegerField()
    description = models.CharField(max_length=500)




