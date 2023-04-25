from django.contrib import admin
from .models import UserAccount
from .models import Complaint

# Add UserAccount Model to Admin Page
admin.site.register(UserAccount)

# Add Complain Model to Admin Page
admin.site.register(Complaint)

