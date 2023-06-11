from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser
from decimal import *

# User
from django.contrib.auth.models import User
import uuid   # generate random num for URL


# Worker Model
class Worker(models.Model):
    name = models.CharField(max_length=100)
    user_accounts = models.ManyToManyField('UserAccount', related_name='workers')

    def __str__(self):
        return self.name

# User Model
class UserAccount(models.Model):

    # instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # add filed
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    random_url = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)   # Unique URL for a user
    worker = models.ForeignKey(Worker, null=True, blank=True, on_delete=models.SET_NULL)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00))

    def __str__(self):
        return self.user.username

    def generate_unique_url(self):
        url_uuid = uuid.uuid4()
        self.random_url = url_uuid
        self.save()
        return url_uuid


class BikeInfo(models.Model):

    BikeCode = models.CharField(primary_key=True, max_length=20)    # Bike Id
    BikeName = models.CharField(max_length=20)                      # Bike name
    BikeType = models.CharField(max_length=20)                      # Bike Type
    Descriptions = models.CharField(max_length=300)                 # Bike Description
    isBroken = models.BooleanField(default=False)                   # Bike is broken or not
    image = models.ImageField(upload_to="static/BikesImage", height_field=None, width_field=None, max_length=100, default='')


class Complaint(models.Model):
    # complaint_id = models.CharField(primary_key=True, max_length=20)     # Complaint Id
    user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)   # One-to-many relation
    Descriptions = models.CharField(max_length=300)                      # Description


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


