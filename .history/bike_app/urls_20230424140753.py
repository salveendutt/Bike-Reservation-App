from django.urls import path
from . import views
from .views import Reservation_Page

app_name = 'bike_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('reserve/', Reservation_Page.as_view(), name='reserve'),
    # path('register', views.AccountRegistration.as_view(), name='register'),
    # path('', views.Login, name='login'),
    # path('logout', views.Logout, name="logout"),
]
