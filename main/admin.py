from django.contrib import admin
from main.models import * 
ListModels = [Mjesto, Event,]

admin.site.register(ListModels)