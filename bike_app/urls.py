from django.urls import path
from . import views

app_name = 'bike_app'

urlpatterns = [
    # path('', views.home, name='home'),
    path('feedback/', views.FeedBack_page, name='feedback'),
    path('', views.Welcome_page),
]
