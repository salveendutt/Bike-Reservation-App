from django.urls import path
from . import views
from .views import Reservation_Page

app_name = 'bike_app'

urlpatterns = [
    path('', views.Welcome_page),
    # path('reserve/', Reservation_Page.as_view(), name='reserve'),
    path('bike_list/', views.bike_list, name='bike_list'),
    # path('register', views.AccountRegistration.as_view(), name='register'),
    # path('', views.Login, name='login'),
    # path('logout', views.Logout, name="logout"),
]
