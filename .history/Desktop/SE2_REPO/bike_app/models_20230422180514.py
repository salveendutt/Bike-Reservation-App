from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
import uuid   # generate random num for URL

# Create your models here.

# User already has fields such as username, password, and email address
class UserAccount(models.Model):

    # instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # add filed
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    random_url = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

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
    isFix=models.BooleanField(default=False)                          # Bike fix or not
"""
class AdminInfo(models.Model):
    admin_id = models.CharField(max_length=20,unique=True)          # Admin Id
    admin_email = models.CharField(max_length=20)                   # Admin Email
    admin_password = models.CharField(max_length=20)                # Admin Password
    admin_login = models.CharField(max_length=50)                   # Admin Login
"""

class Complaint(models.Model):
    complaint_id = models.CharField(primary_key=True, max_length=20)   # Complaint Id
    Descriptions = models.CharField(max_length=300)                    # Description


class Reservation(models.Model):
    Reservation_id = models.CharField(primary_key=True, max_length=20)  # Reservation Id
    Reservation_DateRequest = models.CharField(max_length=30)           # Reservation RequestStartDate
    Reservation_DateEnd = models.CharField(max_length=30)               # Reservation RequestEndDate
    Reservation_Bike = models.CharField(max_length=20)                  # bike Id
    Reservation_status = models.CharField(max_length=20)                # status


