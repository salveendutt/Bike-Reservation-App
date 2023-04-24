"""SE2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bike_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Welcome_page),
    path('login/', include('bike_app.urls', namespace='bike_app')), 
    # path('', include('bike_app.urls')) ,# If it is no path => Going bike_app/urls.py
    # If we want to add something, then better add urls in bike_app/urls.py
]


