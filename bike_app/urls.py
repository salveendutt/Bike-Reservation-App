from django.urls import path
from . import views
from .views import Reservation_Page

app_name = 'bike_app'

urlpatterns = [
    # Welcome page before user log in
    path('', views.welcome),

    # Welcome page after user login
    path('welcome/<uuid:url_uuid>', views.welcome_user, name='welcome_user'),  # unique URL

    # Register page
    path('register', views.AccountRegistration.as_view(), name='register'),

    # Login Page
    path('login', views.Login, name='login'),

    # Logout page
    path('logout', views.Logout, name="logout"),

    # Feedback Page
    path('feedback/<uuid:url_uuid>', views.FeedBack_page, name='feedback'),  # unique URL

    # Bike List page
    # path('bike_list/<uuid:url_uuid>', views.bike_list, name='bike_list'),    # unique URL

    # Reservation page
    path('reserve/', Reservation_Page.as_view(), name='reserve'),

    # Bike List Page
    path('bikeList/<uuid:url_uuid>', views.bikeList_page, name='bikeList'),

    # Q&A
    path('FAQ/', views.FAQ, name='FAQ'),
]