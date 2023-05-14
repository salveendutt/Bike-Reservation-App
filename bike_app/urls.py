from django.urls import path
from . import views
from .views import Reservation_Page

app_name = 'bike_app'

urlpatterns = [
    path('feedback/', views.FeedBack_page, name='feedback'),
    path('', views.Welcome_page),


    path('reserve/', Reservation_Page.as_view(), name='reserve'),

    path('add_complaint/',views.add_complaint),
    path('bikeList/',views.bikeList_page),

]
