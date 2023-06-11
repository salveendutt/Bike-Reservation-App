from django.urls import path
from . import views
from .views import ReservationPage, ReservationCreate, ReservationUpdate, ReservationList, ReservationDelete

app_name = 'bike_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('reservations/', ReservationList.as_view(), name='reservations'),
    path('reserve/', ReservationCreate.as_view(), name='reserve'),
    path('reservation/<int:pk>/', ReservationPage.as_view(), name='reservation'),
    path('reservation-update/<int:pk>/', ReservationUpdate.as_view(), name='reservation-update'),
    path('reservation-delete/<int:pk>/', ReservationDelete.as_view(), name='reservation-delete'),
]
