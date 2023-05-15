from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=30)        # name
    surname = models.CharField(max_length=30)     # surname
    email = models.EmailField(unique=True)        # email address
    password = models.CharField(max_length=128)   # password

    USERNAME_FIELD = 'email'


class BikeInfo(models.Model):
    BikeCode = models.CharField(primary_key=True, max_length=20)    #Bike Id
    BikeName = models.CharField(max_length=20)                      #Bike name
    BikeType = models.CharField(max_length=20)                      #Bike Type
    Descriptions = models.CharField(max_length=300)                 #Bike Description
    BikePicture = models.CharField(max_length=20)                   #Bike Picture path
    isFix=models.BooleanField(default=False)                          # Bike fix or not


class AdminInfo(models.Model):
    admin_id = models.CharField(max_length=20,unique=True)                        #Admin Id
    admin_email = models.CharField(max_length=20)                   #Admin Email
    admin_password = models.CharField(max_length=20)                #Admin Password
    admin_login = models.CharField(max_length=50)                   #Admin Login


class Complaint(models.Model):
    complaint_id = models.CharField(primary_key=True,max_length=20,unique=True)   #Complaint Id
    Descriptions = models.CharField(max_length=300)                    #Description


class Reservation(models.Model):
    BIKE_CHOICES = [
        ('bike1', 'Bike 1'),
        ('bike2', 'Bike 2'),
        ('bike3', 'Bike 3')
    ]
    Reservation_id = models.CharField(primary_key=True, max_length=20)  #Reservation Id
    Reservation_DateRequest = models.CharField(max_length=30)           #Reservation RequestStartDate
    Reservation_DateEnd = models.CharField(max_length=30)               #Reservation RequestEndDate
    Reservation_Bike = models.CharField(max_length=20, choices=BIKE_CHOICES) #bike Id
    Reservation_status = models.CharField(max_length=20)                #status
    Reservation_Number = models.CharField(max_length=5)


