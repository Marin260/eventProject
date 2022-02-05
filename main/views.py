from django.contrib.auth.hashers import make_password
from .forms import AdminSingUpForm
from django.shortcuts import render
from .models import *

def homepage(request):
    events = Event.objects.all()
    context = {'events' : events}
    return render(request, "./base_generic.html", context)

def signUp(request):
    form  = AdminSingUpForm()
    context = {'form' : form}

    if request.method == "POST":
        form = AdminSingUpForm(request.POST)

        if form.is_valid():
            form.cleaned_data['password'] = make_password(form.cleaned_data['password'], None)
            form.save()

    return render(request, "main/signUp.html", context=context)

def login(request):
    return render(request, "main/login.html")