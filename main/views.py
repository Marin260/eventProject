from django.shortcuts import render
from .models import *

def homepage(request):
    events = Event.objects.all().order_by('-date_posted')
    context = {'events' : events}
    return render(request, "./base_generic.html", context)

