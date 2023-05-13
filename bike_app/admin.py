from django.contrib import admin
from .models import UserAccount, Complaint, BikeInfo

# Add UserAccount Model to Admin Page
admin.site.register(UserAccount)

# Add Complain Model to Admin Page
admin.site.register(Complaint)

# Add Bike Model to Admin Page
admin.site.register(BikeInfo)

