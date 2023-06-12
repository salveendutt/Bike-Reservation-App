from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser
from decimal import *
from django.utils import timezone

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
    image = models.ImageField(height_field=None, width_field=None, max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.00))

class Complaint(models.Model):
    # complaint_id = models.CharField(primary_key=True, max_length=20)     # Complaint Id
    user = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)   # One-to-many relation
    Descriptions = models.CharField(max_length=300)                      # Description


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default=None)
    bike = models.ForeignKey(BikeInfo, on_delete=models.CASCADE, default=None)
    start_day = models.DateField(default=timezone.now)
    finish_day = models.DateField(default=timezone.now)
    insurance = models.BooleanField(default=False)
    delivery_method = models.CharField(
        max_length=10,
        choices=(
            ('pick_up', 'Pick Up'),
            ('delivery', 'Delivery')
        ),
        default='pick_up'
    )
    pickup_point = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=(
            ('Warszawa Zachodnia', 'Warszawa Zachodnia'),
            ('Warszawa Centralna', 'Warszawa Centralna'),
            ('Warszawa Wschodnia', 'Warszawa Wschodnia')
        ),
        default='Warszawa Centralna'
    )


