from django.urls import path
from . import views
from .views import Reservation_Page

app_name = 'bike_app'

urlpatterns = [
    path('feedback/', views.FeedBack_page, name='feedback'),
    path('', views.Welcome_page),
    path('bike_info1/', views.bike_info1, name='bike_info1'),
    path('bike_info2/', views.bike_info2, name='bike_info2'),
    path('bike_info3/', views.bike_info3, name='bike_info3'),
    path('bike_info4/', views.bike_info4, name='bike_info4'),
    path('bike_info5/', views.bike_info5, name='bike_info5'),
    path('bike_info6/', views.bike_info6, name='bike_info6'),
    # path('bike_list/', views.bike_list, name='bike_list'),
    path('recharge/', views.recharge, name='recharge'),
    path('FAQ/',views.FAQ, name='FAQ'),

    path('reserve/', Reservation_Page.as_view(), name='reserve'),

    path('add_complaint/',views.add_complaint),
    path('bikeList/',views.bikeList_page),

]
