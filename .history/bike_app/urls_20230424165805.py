from django.urls import path
from . import views
from .views import Reservation_Page

app_name = 'bike_app'

urlpatterns = [
    path('feedback/', views.FeedBack_page, name='feedback'),
    path('', views.Welcome_page),
    path('bike_list/', views.bike_list, name='bike_list'),
    path('reserve/', Reservation_Page.as_view(), name='reserve'),
]
