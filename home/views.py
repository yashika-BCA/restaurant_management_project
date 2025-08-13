from django.conf import settings
from django.shortcuts import render

def homepage(request):
    name = settings.RESTAURANT_NAME
    return render(request, 'home.html' {'restaurant_name': name})




