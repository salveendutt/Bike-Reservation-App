from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Welcome_page(request):
    #find it on templates DIR of app DIR
    return render(request, "welcome.html")