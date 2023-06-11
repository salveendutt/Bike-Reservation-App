from django.contrib import admin
from .models import UserAccount, Complaint, BikeInfo, Worker

# Add UserAccount Model to Admin Page
admin.site.register(UserAccount)

# Add Complain Model to Admin Page
admin.site.register(Complaint)

# Add Bike Model to Admin Page
# admin.site.register(BikeInfo)

class BikeInfo_Mechanic(admin.ModelAdmin):
    list_display = ['BikeCode', 'BikeName', 'BikeType', 'Descriptions', 'isBroken']
    list_editable = ['isBroken']
    list_filter = ['isBroken']

admin.site.register(BikeInfo, BikeInfo_Mechanic)


admin.site.register(Worker)
