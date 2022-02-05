from django.shortcuts import render
from .models import *

def homepage(request):
    events = Event.objects.all()
    context = {'events' : events}
    return render(request, "./base_generic.html", context)

