from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reservation
from django.urls import reverse_lazy
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from django.contrib import messages 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Welcome_page(request):
    #find it on templates DIR of app DIR
    return render(request, "welcome.html")

class ReservationCreate(CreateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('reservations')
    #template_name = 'bike_app/reservation.html'

class ReservationPage(DetailView):
    model = Reservation
    context_object_name = 'reservation'

class ReservationList(ListView): 
    model = Reservation
    context_object_name = 'reservations'

class ReservationUpdate(UpdateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('bike_app:reservations')

class ReservationDelete(DeleteView):
    model=Reservation
    context_object_name='reservation'
    success_url=reverse_lazy('reservations')
