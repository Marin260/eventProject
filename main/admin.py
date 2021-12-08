from django.contrib import admin
from main.models import * 
ListModels = [Mjesto, AdminKorisnici, Event, Objava, Korisnik]

admin.site.register(ListModels)