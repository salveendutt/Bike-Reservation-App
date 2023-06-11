from django.urls import path
from . import views
from .views import ReservationPage, ReservationCreate, ReservationUpdate, ReservationList, ReservationDelete


app_name = 'bike_app'

urlpatterns = [
    path('feedback/', views.FeedBack_page, name='feedback'),
    path('', views.Welcome_page),
    #path('bike_list/', views.bike_list, name='bike_list'),
    #path('reserve/', Reservation_Page.as_view(), name='reserve'),

    path('add_complaint/',views.add_complaint),
    path('bikeList/',views.bikeList_page),

#Reservation Part
    path('reservations/', ReservationList.as_view(), name='reservations'),
    path('reserve/', ReservationCreate.as_view(), name='reserve'),
    path('reservation/<int:pk>/', ReservationPage.as_view(), name='reservation'),
    path('reservation-update/<int:pk>/', ReservationUpdate.as_view(), name='reservation-update'),
    #path('reservation-delete/<int:pk>/', ReservationDelete.as_view(), name='reservation-delete'),
    path('reservation-delete/<int:pk>/', ReservationDelete.as_view(), name='reservation-delete'),
    #path('edit/<str:reservation_id>/', ReservationUpdate.as_view(), name='reservation-update'),

]
