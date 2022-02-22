from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import *
from main.models import Event
from django.contrib.auth.mixins import UserPassesTestMixin


class ProfileDetailView(UserPassesTestMixin, DetailView):
    model = Profile

    def test_func(self):
        UserName= self.kwargs.get("username")
        tmp = get_object_or_404(User, username=UserName)
        post = self.get_object()
        if self.request.user == tmp:
            if Profile.objects.filter(user=tmp).exists():
                print ("Ovaj user ima profil")
            else:
                print ("Ovaj user nema profil")
                noviProfil = Profile(user=tmp)
                noviProfil.save()
            return True
        return True
    
    def get_object(self):
        """
        Get username in url instead of id
        """
        
        UserName= self.kwargs.get("username")
        


        #if Profile.objects.filter(id=get_object_or_404(User, id=tmp).id).exists():
        #    print("It exists")
        #else:
        #    print("Ne postoji")
        
        return get_object_or_404(User, username=UserName)

    def get_context_data(self, **kwargs):
        """
        Get extra context for display in detail view
        extra context: all the events created by the user detailed user
        """
        context = super().get_context_data(**kwargs)
        allEvents = Event.objects.filter(autor_objave__username=self.get_object())
        context['event_list'] = allEvents
        context['event_count'] = allEvents.count()
        return context
