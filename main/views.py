from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
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
    fields = ['naziv_eventa', 'opis_eventa', 'datum_odrzavanja', 'vrijeme_odrzavanja', 'placanje_ulaza', 'cijena_ulaza', 'mjesto_odrzavanja', 'adresa', 'slika']

    def form_valid(self, form):
        form.instance.autor_objave = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['naziv_eventa', 'opis_eventa', 'datum_odrzavanja', 'vrijeme_odrzavanja', 'placanje_ulaza', 'cijena_ulaza', 'mjesto_odrzavanja', 'adresa', 'slika']

    def form_valid(self, form):
        #insert the curnet loged in user as event author
        form.instance.autor_objave = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        UserPassesTestMixin will run this function to test if
        current loged in user is the event author
        403 Forbidden if he is not the author
        """
        post = self.get_object()
        if self.request.user == post.autor_objave:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/' #redirect to /

    """
    UserPassesTestMixin will run this function to test if
    current loged in user is the event author
    403 Forbidden if he is not the author
    """
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor_objave:
            return True
        return False


class AuthorProfileDetailView(DetailView):
    model = User

    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(User, username=UserName)


def landing(request):
    return render(request, 'landing.html')

def emptyRedirect(request):
    if request.user.is_authenticated:
        return redirect('main_homepage')
    else:
        return redirect('account_login')


def handler404(request, *args, **argv):
    #custom 404
    return render(request, '404.html')
    
def handler403(request, *args, **argv):
    #custom 403
    return render(request, '403.html')