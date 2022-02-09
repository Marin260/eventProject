from unittest import result
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from .models import *

def homepage(request):
    events = Event.objects.all().order_by('-date_posted')
    context = {'events' : events}
    return render(request, "./main/home.html", context)

@login_required
def addPeopleToEvent(request):
    """
    AJAX request view
    on request check if method is POST
    retrive an object with the recived id (eventid) -> model_field indicates the field inside event model 
    check if the user exists in many to many field
    if it does, remove it and decrease total amount
    else do the inverse... save final 
    """
    if request.POST.get('action') == 'post':
        result = ''
        event_id = int(request.POST.get('eventid'))
        model_field = int(request.POST.get('modelField'))
        event = get_object_or_404(Event, id=event_id) # try: get object with that id or raise err

        if model_field == 1:
            if event.dolaze.filter(id=request.user.id).exists():
                event.dolaze.remove(request.user)
                event.broj_dolaze -= 1
            else:
                event.dolaze.add(request.user)
                event.broj_dolaze += 1
            result = event.broj_dolaze
        else:
            if event.zainteresirani.filter(id=request.user.id).exists():
                event.zainteresirani.remove(request.user)
                event.broj_zainteresiranih -= 1
            else:
                event.zainteresirani.add(request.user)
                event.broj_zainteresiranih += 1
            result = event.broj_zainteresiranih
        event.save()
        return JsonResponse({'result':result})


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['naziv_eventa', 'opis_eventa', 'datum_odrzavanja', 'vrijeme_odrzavanja', 'placanje_ulaza', 'cijena_ulaza', 'mjesto_odrzavanja', 'adresa']

    def form_valid(self, form):
        form.instance.autor_objave = self.request.user
        return super().form_valid(form)
    
