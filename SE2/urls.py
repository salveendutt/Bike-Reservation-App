from django.contrib import admin
from django.urls import path, include
from bike_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bike_app.urls', namespace='bike_app')),  # If there is no path => Going bike_app/urls.py
    # If we want to add something, then better add urls in bike_app/urls.py
]


