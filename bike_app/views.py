from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Reservation
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Welcome_page(request):
    #find it on templates DIR of app DIR
    return render(request, "welcome.html")

class Reservation_Page(CreateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'bike_app/reservation.html'
